## IFRS_UNSPSC

IFRS Accounts and UNSPSC Item Groups

This application is intended to make it very easy for an ERPNext user to:
 Add IFRS accounts heads for Financial Statements.
 Add UNSPSC Item Groups.

Upon installation, user will a fairly complete set of UNSPSC Item Groups as well as our interpretations of a typical IFRS Chart of Accounts for SME's.

### IFRS Accounts
International Financial Reporting Standards Foundation is the publisher of this chart of accounts or taxonomy. A taxonomy classifies information to make it clearer and easire to understand this information.  IFRS
Most of the acocunts created are group accounts (parent accounts), thus all that is necessary is for the user to move existing account heads into the IFRS account groups, one by one. This process cannot be automated due to the sensitive nature of business accounts.

Please note: It does not include complete Taxonomy and support for XBRL, notes, etc.  just a Chart of Accounts!

What are IFRS Accounts and why should they interest me?

"International Financial Reporting Standards, usually called IFRS, are standards issued by the IFRS Foundation and the International Accounting Standards Board (IASB) to provide a common global language for business affairs so that company accounts are understandable and comparable across international boundaries." -  [Wikipedia](https://en.wikipedia.org/wiki/International_Financial_Reporting_Standards)

[IFRS Taxonomy](https://www.ifrs.org/issued-standards/ifrs-taxonomy/)
[IFRS Standards for SME](https://www.ifrs.org/issued-standards/ifrs-for-smes/)

[Any use of this is subject to the Terms of Use and Website Terms and the copyright notice and disclaimer found on this link]https://www.ifrs.org/-/media/feature/about-us/legal-and-governance/legal-docs/taxonomy/taxonomy-legal.pdf?la=en

### UNSPSC
UNSPSC: United Nations Standard Product Services Code
"The United Nations Standard Products and Services Code (UNSPSC) is a hierarchical convention that is used to classify all products and services. It is the most efficient, accurate and flexible classification system available today for achieving company-wide visibility of spend analysis, enabling procurement to deliver on cost-effectiveness demands and allowing full exploitation of electronic commerce capabilities."

The codeset is open sourced, albeit through paid memberships. However, it is a product centric coding scheme, which is aimed to "be used [without any use restrictions or licensing fees](http://www.unspsc.org/faqs#How%20does%20UNSPSC%20differ%20from%20NAIC%20and%20SIC)"

[Terms of use in FAQ](http://www.unspsc.org/faqs#How%20does%20UNSPSC%20differ%20from%20NAIC%20and%20SIC)


## Requirements
Your ERPNext instance needs to be setup and configured, ready to go, with at least one company configured.
The Default company will be the one for which the accounts are created. You can check which company is setup 
in ERPNext, prior to installing this application.

    Setup > Global Settings > Default Company (`default_company`)

#### License

MIT