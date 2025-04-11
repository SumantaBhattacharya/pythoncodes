#https://pypi.org/project/pywhatkit/
#pip install pywhatkit
#pip install flask
import pywhatkit as pw
text='''Beauty lies in the eye of beholder
the apple doesnt fall far from the tree
prevention is better than cure
first learn to love yourself before loving others
Hare ram hare ram ram ram hare hare hare krishna hare krishna krishna krishna hare hare
"Everyone is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid," 
 '''

txt=pw.text_to_handwriting(text,'demo1.png',[0.0,1,138])#text,filename under single quotation,colour under square bracket
print("End")
