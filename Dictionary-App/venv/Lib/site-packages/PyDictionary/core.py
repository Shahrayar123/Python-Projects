from __future__ import print_function
import sys, re, goslate
try:
    from .utils import _get_soup_object
except:
    from utils import _get_soup_object

python2 = False
if list(sys.version_info)[0] == 2:
    python2 = True

class PyDictionary(object):

    def __init__(self, *args):
        try:
            if isinstance(args[0], list):
                self.args = args[0]
            else:
                self.args = args
        except:
            self.args = args

    
    def printMeanings(self):
        dic = self.getMeanings()
        for key in dic.keys():
            print(key.capitalize() + ':')
            for k in dic[key].keys():
                print(k + ':')
                for m in dic[key][k]:
                    print(m)

    def printAntonyms(self):
        antonyms = dict(zip(self.args,self.getAntonyms(False)))
        for word in antonyms:
            print(word+':')
            print(', '.join(antonyms[word]))

    def printSynonyms(self):
        synonyms = dict(zip(self.args,self.getSynonyms(False)))
        for word in synonyms:
            print(word+':')
            print(', '.join(synonyms[word]))

    def getMeanings(self):
        out = {}
        for term in self.args:
            out[term] = self.meaning(term)
        return out

    def translateTo(self, language):
        return [self.translate(term, language) for term in self.args]

    def translate(self, term, language):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                gs = goslate.Goslate()
                word = gs.translate(term, language)
                return word
            except:
                print("Invalid Word")

    def getSynonyms(self, formatted=True):
        return [self.synonym(term, formatted) for term in self.args]

    def __repr__(self):
        return "<PyDictionary Object with {0} words>".format(len(self.args))

    def __getitem__(self, index):
        return self.args[index]

    def __eq__(self):
        return self.args

    def getAntonyms(self, formatted=True):
        return [self.antonym(term, formatted) for term in self.args]

    @staticmethod
    def synonym(term, formatted=False):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                data = _get_soup_object("https://www.synonym.com/synonyms/{0}".format(term))
                section = data.find('div', {'class': 'type-synonym'})
                spans = section.findAll('a')
                synonyms = [span.text.strip() for span in spans]
                if formatted:
                    return {term: synonyms}
                return synonyms
            except:
                print("{0} has no Synonyms in the API".format(term))


    @staticmethod
    def antonym(term, formatted=False):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                data = _get_soup_object("https://www.synonym.com/synonyms/{0}".format(term))
                section = data.find('div', {'class': 'type-antonym'})
                spans = section.findAll('a')
                antonyms = [span.text.strip() for span in spans]
                if formatted:
                    return {term: antonyms}
                return antonyms
            except:
                print("{0} has no Antonyms in the API".format(term))

    @staticmethod
    def meaning(term, disable_errors=False):
        if len(term.split()) > 1:
            print("Error: A Term must be only a single word")
        else:
            try:
                html = _get_soup_object("http://wordnetweb.princeton.edu/perl/webwn?s={0}".format(
                    term))
                types = html.findAll("h3")
                length = len(types)
                lists = html.findAll("ul")
                out = {}
                for a in types:
                    reg = str(lists[types.index(a)])
                    meanings = []
                    for x in re.findall(r'\((.*?)\)', reg):
                        if 'often followed by' in x:
                            pass
                        elif len(x) > 5 or ' ' in str(x):
                            meanings.append(x)
                    name = a.text
                    out[name] = meanings
                return out
            except Exception as e:
                if disable_errors == False:
                    print("Error: The Following Error occured: %s" % e)

if __name__ == '__main__':
    d = PyDictionary('honest','happy')
    d.printSynonyms()

