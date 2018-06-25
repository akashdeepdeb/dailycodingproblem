'''
input: 
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

output: 
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
'''
import pprint

pp = pprint.PrettyPrinter(indent=4)

def flatten(out, inp, s):
	for obj in inp:
		if type(inp[obj]) is not dict:
			new_s = s + '.' + obj
			out[new_s[1:]] = inp[obj]
		elif type(inp[obj]) == dict:
			flatten(out, inp[obj], s+'.'+obj)

def main():
	inp1 = {
    	"key": 3,
    	"foo": {
        	"a": 5,
        	"bar": {
            	"baz": 8
        	}
    	}
	}
	inp2 = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
	out = dict()
	flatten(out, inp1, '')
	pp.pprint(out)

main()
