var txt="hi helloo hey hyy hi hey"
var dict={}
var word_arr=txt.split(" ")
for(let word of word_arr)
{
    if(word in dict)
    dict[word]+=1
    else
    dict[word]=1
}
console.log(dict);
