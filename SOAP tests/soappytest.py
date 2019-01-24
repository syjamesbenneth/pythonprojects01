import requests
url="https://ws.xpressmoney.biz/XMWS/services/XMSSendTxnService?wsdl"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/soap+xml'}
body = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsd="http://services.xm.org/xsd">
<soap:Header/>
<soap:Body>
<xsd:getXMRateCalculateDetails>
<xsd:authenticationAgentCode>UAEEXAEAU001</xsd:authenticationAgentCode>
<xsd:userID>10001cashier</xsd:userID>
<xsd:password>test123</xsd:password>
<xsd:pin>mam123</xsd:pin>
<xsd:amount>80</xsd:amount>
<xsd:deliveryOption>PS</xsd:deliveryOption>
<xsd:sendingAgentCode>UAEEXAEAU001</xsd:sendingAgentCode>
<xsd:fromCountry>AE</xsd:fromCountry>
<xsd:fromCcy>AED</xsd:fromCcy>
<xsd:receivingAgentCode>XMANYINKL001</xsd:receivingAgentCode>
<xsd:toCcy>INR</xsd:toCcy>
<xsd:toCountry>IN</xsd:toCountry>
<xsd:includeCharges>Y</xsd:includeCharges>
<xsd:paymentMode>CS</xsd:paymentMode>
<xsd:transactionSource>1</xsd:transactionSource>
<xsd:serviceProvider>UAEEXAE#####</xsd:serviceProvider>
<xsd:xmReserved1></xsd:xmReserved1>
<xsd:xmReserved1></xsd:xmReserved2>
<xsd:xmReserved1></xsd:xmReserved3>
<xsd:xmReserved1></xsd:xmReserved4>
</xsd:getXMRateCalculateDetails>
</soap:Body>
</soap:Envelope>""""


response = requests.post(url,data=body,headers=headers)
print response.content