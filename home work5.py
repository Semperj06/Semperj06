# Exercise 1.
'''days ={
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}
enter = int(input("Enter day "))
print(days.get(enter,("You wrong")))'''
# Exercise 2.
'''cat ={
    "name": str(input("print name")),
    "breed": "bengal cat",
    "age": "4 mounth",
    "color": "ginger",
}
print(cat)'''
# Exercise 3.
'''text = str(input("Print text "))
statistics = {}
for item in text:
    if item in statistics:
        statistics[item] += 1
    else:
        statistics[item] = 1

print(statistics)'''

'''url = """</style><div class=sc-m6le0i-14 sc-wrmhla-0 kZABMJ bftPz><div class="sc-m6le0i-15 btgqQN"><div class="sc-m6le0i-14 kZABMJ"><h2>Sorry, the page youre looking for was not found.</h2></div><div class="sc-m6le0i-14 kZABMJ"><h3 class="sc-wrmhla-1 cgioLQ">Here are some helpful links instead</h3></div><div class="sc-m6le0i-14 kZABMJ"><ul class="sc-wrmhla-2 cQHVXY"><li><a href="/" class="sc-j2jiwi-0 hxrYKN">Home</a></li><li><a href="/stocks" class="sc-j2jiwi-0 hxrYKN">Browse for companies</a></li><li><a href="/discover/sample-portfolios" class="sc-j2jiwi-0 hxrYKN">Browse sample portfolios</a></li><li><a href="/discover/investing-ideas" class="sc-j2jiwi-0 hxrYKN">Discover investing ideas</a></li><li><a href="https://support.simplywall.st/hc/en-us">Learning centre</a></li></ul></div><div class="sc-m6le0i-14 kZABMJ"><p><span>If you think you&#x27;re seeing this page in error </span><a href="mailto:feedback@simplywallst.com">send us an email</a><span> to let us know!</span></p></div></div></div></div><script>window.REDUX_STATE = {"analysts":{"brokersMap":{},"analystMap":{}},"averages":{},"company":{"competitors":{},"formatting":{},"news":{},"events":{},"statements":{},"summary":{},"urlToIdMapping":{},"symbolToIdMapping":{},"analysis":{},"management":{},"insiderTransactions":{},"insiderTransactionsMap":{},"listings":{},"analysts":{},"topShareholders":{}},"grid":{"companies":{},"views":{"explore":[],"user":[],"entities":{},"exploreTotal":0}},"events":undefined,"industryAverages":{"fields":{"keys":[],"entities":new Map([])},"constituents":{"keys":[],"entities":new Map([])},"averagesByCountry":{"keys":[],"entities":new Map([])},"lastUpdatedTracker":{"keys":[],"entities":new Map([])}},"insiderTransactions":undefined,"newsNext":undefined,"page":{"pageStatus":404,"current":"NotFound"},"people":{},"portfolio":{"currentId":null,"companyToAddToPortfolioHoldings":"","isUpdatingItemPrice":false,"itemPriceMap":{},"doesPortfolioNeedRefresh":true,"isAddingTransaction":false,"isUpdatingTransactions":false,"transactionsStatus":"idle","transactionsModalStatus":"hidden","transactionsCurrentItemId":"","deleteHoldingModal":{"companyId":"","companyName":"","portfolioId":"","uniqueSymbol":"","deleteHoldingModalStatus":"hidden"},"editPortfolioModal":{"editStatus":"idle","editPortfolioModalStatus":"hidden"}},"portfolios":{"entities":{},"holdingsTable":{},"holdingsItemIdToCompanyIdMap":{},"publicKeys":[],"transactionsTable":{},"userKeys":[],"news":{}},"priceChart":undefined,"ssr":undefined,"ui":{"reload":false,"message":"","loading":false,"emailCheck":false,"emailExists":null,"emailType":"none","emailAddressChecked":"","sidebarOpen":false,"onboarded":true,"appLevelError":false,"appVersion":"","fileIsDownloading":false,"hasSeenSnowflakeIntroduction":true,"appError":false,"appErrorMessage":"","addRemoveCompanyModalStatus":"hidden","authenticationStatus":0,"analystsFetchStatus":"idle","analystsModalStatus":"hidden","updatingHoldingsStatus":"idle","updatingPortfolioStatus":"idle","searchStatus":"idle","isFetchingUserBilling":false,"gridIsLoading":false,"fetchingCompany":"fetching","portfolioListIsFetching":false,"accountRecoveryErrorMessage":"","accountRecoverStatus":"idle","loginOtpErrorMessage":"","preDeleteAccountStatus":"idle","deleteAccountStatus":"idle","deleteAccountErrorMessage":"","fetchPublicPortfolioState":"idle","gridSaveState":"idle","fetchStatementsStatus":"uninitialised","companiesFetchStatus":"idle","ideaFetchStatus":"idle","fileIsUploading":false,"accountConvertStatus":0,"accountTypeChangeStatus":0,"accountTypeChangeMessage":"","cfIpCountry":"ua"}}</script><script>window.__REACT_QUERY_STATE__ = {"mutations":[],"queries":[]}</script><script id="__LOADABLE_REQUIRED_CHUNKS__" type="application/json">[1597]</script><script id="__LOADABLE_REQUIRED_CHUNKS___ext" type="application/json">{"namedChunks":["components-NotFound"]}</script>
<script async defer data-chunk="main" src="/static/runtime~main.modern.9fe5b2b9.js"></script>
<script async defer data-chunk="main" src="/static/vendor.modern.810ce56f.js"></script>
<script async defer data-chunk="main" src="/static/main.modern.217d2298.js"></script>
<script async defer data-chunk="components-NotFound" src="/static/OTPLoginContainer.modern.588ebccf.js"></script><script data-rh="true" async="true" defer="true" src="https://swttkpx937lg.statuspage.io/embed/script.js"></script><script type="text/javascript">"""
tags = ["div", "p", "script","/style","/h2","h2","/script", "/h3", "/div","/body","h3", "ul", "li", "a","/a", "/li", "/ul", "/span", "/p", "span" ]
tags_1 = ["h2", "a", "li", "ul", "span", "p", "h2", "script", "h3", "div", "body"]
for elem in tags:
    while f'<{elem}' in url:
        strt = url.find(f'<{elem}')
        stp = url.find(">", strt)
        url = url.replace(url[strt: stp+1], "")

for elem in tags_1:
    while f'</{elem}' in url:
        strt = url.find(f'</{elem}')
        stp = url.find(elem, strt)
        url = url.replace(url[strt: stp+1], "")
print(url)'''