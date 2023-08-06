
def createSite(title,bodyCont,codeType):
    document =  '''<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title><{tit}></title>\n</head>\n<body><{body}></body>\n</html>'''
    if codeType == 'view':
        document = document.replace("<{tit}>",title)
        replacement = (bodyContent(bodyCont, replaceString))
        document =  document.replace("<{body}>",replacement)
        print(document)
    elif codeType == 'file':
        pass

HEADING_TOKEN = ['h1','h2','h3','h4','h5','h6']
HTML_TAG_TOKENS = ['p','a','img','ul','ol','li','table','tr','td','th','form','input','button','label','select','option','textarea','div','span','footer','nav','article','section','aside','audio','video','canvas','svg','iframe','script','style']

replaceString = "\n"

def bodyContent(dictDoc,replaceStr):
    for i in dictDoc:
        if i in HEADING_TOKEN or HTML_TAG_TOKENS:
            replaceStr += '    <' + i + '>\n        ' +  str(dictDoc[i]) + '\n    </' + i + '>\n'
    return replaceStr



