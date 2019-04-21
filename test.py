from jpc import Jpc

_file = "test.json"
#pass a string from path where you file exist
data = {
	"hay":{"yoho":"hoyo"}
}
jp = Jpc(_file) #call Class
read = jp.reads #see data from json File
						#you can specifct, data using dot or subscribed
						#e.g read.hello
print(read)