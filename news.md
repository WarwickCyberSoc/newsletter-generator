# Cyber Security news
Some interesting news from the wider world of cyber security. :)

---
## Bad Encryption in Chinese Mobile Apps - What could it mean?
_Risky Business_'s Tom Uren published a [fascinating short read](https://news.risky.biz/chinese-mobile-app-encryption-is-suspiciously-awful/) this week
analysing some research into the top-performing apps in the Mi store, a popular
app store in China.

It found that Chinese apps, in comparison to Google Play apps, were much more
likely to use proprietary, vulnerable cryptographic systems for securing network
data. This was _more_ likely to be the case if an app is particularly popular.

What could this mean? One reasonable explanation could be that the Chinese
government requires app encryption to be intentionally vulnerable for
eavesdropping purposes.

Regardless of that, the lesson to learn for your own projects is clear. Don't
roll your own encryption folks, use something tried and tested. Generally NIST
standards are a good thing to look at if you're deciding on encryption methods
for your next app.


---
## Chrome by default no longer able to run as root
Also from _Risky Business_ (I rather like their work if you couldn't tell),
Catalin Cimpanu has done a [wonderful writeup](https://news.risky.biz/risky-bulletin-chrome-will-de-elevate-itself-when-run-with-admin-privileges/) on a feature newly added to Chrome,
donated by Microsoft.

For those who don't know, Microsoft Edge is based on Chromium, an open-source
browser which is also used as the basis for google Chrome. In 2019 Microsoft
added a feature to Edge which would automatically re-launch the browser if it
was run with admin privileges. They've now donated this feature to Chromium,
so it can now be used by other Chromium-based browsers.

### Why this matters
The big benefit of this change is that it makes it harder for browser-installed
malware to run with admin privileges. If malware is downloaded and executed
through a chrome instance running with admin privileges, the malware inherits
that context.
