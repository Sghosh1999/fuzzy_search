import http.client
import json
import streamlit as st
import collections
import operator
from PIL import Image


#Headers & Titles
st.title("Fuzzy Search Matcher :smile:")
image = Image.open('./images/logo.png')




st.image(image, caption='Sunrise by the mountains')

def fuzzySearch(string_search):
    temp_str = ""
    conn = http.client.HTTPSConnection("google-search3.p.rapidapi.com")
    search_results = []

    headers = {
        'x-rapidapi-key': "fa4bd66f20msh6c7933d1338321fp1a944ejsn9e0436cef9f1",
        'x-rapidapi-host': "google-search3.p.rapidapi.com"
    }

    for i in string_search.split():
        temp_str += i
        temp_str += '+'
    conn.request(
        "GET", f"/api/v1/search/q={temp_str[:-1]}&num=9", headers=headers)

    res = conn.getresponse()
    data = res.read()

    final_serach_response = data.decode("utf-8")

    serach_response = json.dumps(final_serach_response)
    # converting string to json
    responses = json.loads(serach_response)
    final_responses = json.loads(responses)

    for single_res in final_responses['results']:
        search_results.append(single_res['title'])
    return search_results


def search_find2(results):
    list_item = []
    for i in results:
        i = i.replace('&', 'and')
        for j in i.split():
            list_item.append(j)

    a = list(collections.Counter(list_item).values())
    stop_ind = max(a) - (sum(a)/len(a))

    counter_l = collections.Counter(list_item)
    #print(counter_l, stop_ind)

    ans = ""
    for i in counter_l.keys():
        if counter_l[i] > stop_ind:
            ans += i
            ans += " "
    ans = ans.replace('|', "")
    ans = ans.replace('...', "")
    ans = ans.replace('-', "")

    ansfi = ""

    for i in ans.split():
        ansfi += i
        ansfi += " "
    return ansfi[:-1]


def search(string_8):
    return search_find2(fuzzySearch(string_8))



try:
    input = st.text_input("Enter the search field")
    if st.button("Search"):
        st.write(search(input))
except:
    st.warning("Please enter a Serach Phrase")


st.title("Working Principle :nerd_face:")
st.markdown("""---""")
st.write("Step 1: Generating a Bag Of Words of teh Search results")
st.write("Step 2: Calculating Word frequency ofeach words in the Bag Of Words")
st.write("Step 3: Calculating the Stop Index")
st.write("Step 4: Finalizing the results")
st.markdown("""---""")

st.title("Mathematical Formulation :nerd_face:")

st.markdown("**WF** = word frequency of search results")
st.latex(r'''SI (Stop Index) = max(WF) - \frac{\sum_{i=1}^{n} WF}{n}''')

st.latex(r'''f(result String) = \begin{cases}
word(i) & \text{ if } WF(word(i)) > SI \\ 
 skip & \text{ if } WF(word(i)) < SI 
\end{cases}''')







