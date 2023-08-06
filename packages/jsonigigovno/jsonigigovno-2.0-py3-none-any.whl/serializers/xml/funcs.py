from serializers.xml.const import *

def create_xml_element(name: str, data: str, is_first=False):
    if is_first:
        return f"<{name} {XML_SCHEME_SOURCE}>{data}</{name}>"
    else:
        return f"<{name}>{data}</{name}>"
    
def mask_symbols(string: str) -> str:
    return string.replace('&', "&amp;").replace('<', "&lt;").replace('>', "&gt;"). \
                      replace('"', "&quot;").replace("'", "&apos;")
                      
def unmask_symbols(string: str) -> str:
        return string.replace("&amp;", '&').replace("&lt;", '<').replace("&gt;", '>'). \
                      replace("&quot;", '"').replace("&apos;", "'")