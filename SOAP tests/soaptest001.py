import sys
import chilkat

#  Demonstrates how to do a SOAP request using the REST API.

#  This example requires the Chilkat API to have been previously unlocked.
#  See Global Unlock Sample for sample code.

rest = chilkat.CkRest()

#  This is the request to be sent:

/*
POST /WeatherWS/Weather.asmx HTTP/1.1
Host: wsf.cdyne.com
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "http://ws.cdyne.com/WeatherWS/GetCityWeatherByZIP"

<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetCityWeatherByZIP xmlns="http://ws.cdyne.com/WeatherWS/">
      <ZIP>string</ZIP>
    </GetCityWeatherByZIP>
  </soap:Body>
</soap:Envelope>
*/

#  Note: The application does not need to set the Host or Content-Length headers.
#  Chilkat will automatically add these headers.

#  Make the initial connection (without sending a request yet).
bTls = False
port = 80
bAutoReconnect = True
#  In this particular case, it is important to connect to "wsf.cdyne.com", not "ws.cdyne.com"...
success = rest.Connect("wsf.cdyne.com",port,bTls,bAutoReconnect)
if (success != True):
    print(rest.lastErrorText())
    sys.exit()

#  Add request headers:
success = rest.AddHeader("Content-Type","text/xml; charset=utf-8")
success = rest.AddHeader("SOAPAction","http://ws.cdyne.com/WeatherWS/GetCityWeatherByZIP")

#  Build the SOAP XML request body.
soapXml = chilkat.CkXml()

soapXml.put_Tag("soap:Envelope")
success = soapXml.AddAttribute("xmlns:xsi","http://www.w3.org/2001/XMLSchema-instance")
success = soapXml.AddAttribute("xmlns:xsd","http://www.w3.org/2001/XMLSchema")
success = soapXml.AddAttribute("xmlns:soap","http://schemas.xmlsoap.org/soap/envelope/")

soapXml.NewChild2("soap:Body","")
success = soapXml.GetChild2(0)
soapXml.NewChild2("GetCityWeatherByZIP","")
success = soapXml.GetChild2(0)
success = soapXml.AddAttribute("xmlns","http://ws.cdyne.com/WeatherWS/")
soapXml.NewChild2("ZIP","60187")
soapXml.GetRoot2()

print(soapXml.getXml())

#  Send the SOAP request
responseXml = rest.fullRequestString("POST","/WeatherWS/Weather.asmx",soapXml.getXml())
if (rest.get_LastMethodSuccess() != True):
    print(rest.lastErrorText())
    sys.exit()

#  When successful, the response status code will equal 200.
if (rest.get_ResponseStatusCode() != 200):
    #  Examine the request/response to see what happened.
    print("response status code = " + str(rest.get_ResponseStatusCode()))
    print("response status text = " + rest.responseStatusText())
    print("response header: " + rest.responseHeader())
    print("response body (if any): " + responseXml)
    print("---")
    print("LastRequestStartLine: " + rest.lastRequestStartLine())
    print("LastRequestHeader: " + rest.lastRequestHeader())
    sys.exit()

xml = chilkat.CkXml()
success = xml.LoadXml(responseXml)

#  GetXml will emit XML that is nicely indented for human viewing..
print(xml.getXml())

#  A sample response XML is shown below...

#  To get some information, use ChilkatPath.  For example...
print("Temperature: " + xml.chilkatPath("soap:Body|GetCityWeatherByZIPResponse|GetCityWeatherByZIPResult|Temperature|*"))

print("Success.")

