__author__ = 'meramac'

#This works like a function factory and returns a new function whose argument is word. That function will have a particular surrounding
def surround_with(surrounding):
    def surround_with_value(word):
        return "{}{}{}".format(surrounding,word,surrounding)
    return surround_with_value

def transform_words(content,targets,transform):
    result = ''
    for word in content.split():
        if word in targets:
            result += ' {}'.format(transform(word))
        else:
            result += ' {}'.format(word)
    return result


markdown_string = 'I am learning tidbits of Python'
markdown_string_italicized = transform_words(markdown_string, ['Python'],
        surround_with('*'))
print(markdown_string_italicized)