try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

str_xml ='''
<xml>
  <ToUserName><![CDATA[gh_e610e5b114d5]]></ToUserName>
  <FromUserName><![CDATA[oA19euP08Zx7ax3i1j2vq7aHqS4k]]></FromUserName>
  <CreateTime>1459503365</CreateTime>
  <MsgType><![CDATA[event]]></MsgType>
  <Event><![CDATA[SCAN]]></Event>
  <EventKey><![CDATA[1]]></EventKey>
  <Ticket><![CDATA[gQFq8DoAAAAAAAAAASxodHRwOi8vd2VpeGluLnFxLmNvbS9xL3AwTmVVdFhtTU5sSk9zLTFLbTNIAAIEbRr_VgMEgDoJAA==]]></Ticket>
</xml>
'''

tree = ET.fromstring(str_xml)
msg_type = tree.find('./MsgType')

print msg_type.text