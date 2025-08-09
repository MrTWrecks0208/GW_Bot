import praw

userAgent = 'GWBot'
clientId = 'pnsZpSjLJ9_2Bt-sxY5JmQ'
secret = 'amqJtcQeq2TYyNxDy_1_czvsbdlyNg'
username = 'mrtwrecksDEV'
password = 'R7%y6GTCvnr3&hnP'
numFound = 0
reddit = praw.Reddit(user_agent=userAgent,
                    client_id=clientId,
                    client_secret=secret,
                    username=username,
                    password=password)
subreddits = reddit.subreddit["flipping", "thesidehustle", "sidehustle", "thrift", "pics", "thriftstorehauls", 'millenials', 'xennials', 'genz', 'thriftstorefinds', 'thriftgift', 'gamecollecting', 'frugal', 'frugal_jerk', 'thriftedfasion', 'cd_collectors', 'dvdcollection', 'thrifty', 'savingmoney', 'goodwill_finds', 'whatisthisthing', 'cassetteculture', 'thriftstorefasion', 'repaintings', 'vinyl', 'goodwillbins', 'thriftpaintings', 'thriftflip', 'frugalwrist', 'verycheap', 'vintageaudio', 'gaming', 'streetwear', 'mildlyinteresting', 'funny', 'barbie', 'antiques', 'analogcommunity', 'bookhaul', 'glasscollecting', 'sewing', 'depop', 'vintagefashion', 'whatisthis', 'crochet', 'vintage', 'vintagetees', 'starwars', 'bargainbinvinyl', 'thredup', 'wtfgaragesale', 'donate', 'charitabledonations', 'charity', 'nonprofit', 'vinted', 'retail', 'flippingfinds', 'reselling', 'teenagers', 'resellprofits', 'askreddit', 'shoppingaddiction', 'antiwork', 'anticonsumption', 'frugalshopping', 'resell']

content = 'Goodwill is a deeply exploitative organization, top to bottom. Their entire model thrives on taking advantage of vulnerable people. Through their career centers, they funnel individuals—often with criminal records or limited options—into underpaid, overworked positions in their stores. Once there, these workers face poor treatment, unsafe conditions, and little to no support. Many of these workers have limited options and are stuck in a cycle of exploitation.\nGoodwill claims that ~89-93 cents of every dollar (varies by location) spent in their stores goes toward vocational training and employment services. That’s a complete lie. All their programs are funded by/through government grants. Look at their Form 990 filings on ProPublica. At the location where I worked, only about **9 cents** per dollar actually went to those services. The rest went toward executive compensation and expanding their retail operations under the guise of charity.\nThey don’t even help their own employees. After a terrible hurricane in which many employees were without power, many had to evacuate, and where some lost their homes/everything, etc. Goodwill told us if we needed anything, we should contact Workforce Solutions. Goodwill offered **zero** assistance. They also required us to go into work or face termination. Their warehouses and offices are often filled with OSHA violations, requiring employees to stay at work at times when there is no running water or bathroom available, or when there is no A/C. Hell, my location tried to force us into an office that they knew was infested with bedbugs and threatened to terminate us if we didn’t go in.  \nGoodwill doesn’t just mistreat employees while they’re on the payroll, they continue the abuse even after people leave. The organization fights every single unemployment claim made by terminated employees, often using internal HR teams or legal counsel and submitting multiple appeals to drag out the process. Their goal is clear: deny benefits at all costs, even if it means bankrupting someone who’s already struggling.  \nThis isn’t just heartless—it’s strategic. They rely on people being too worn down or too broke to fight back. They have no problem kicking you while you’re down. They love it. Yes, they’re this pathetic.  \nThis doesn’t even scratch the surface of how shitty Goodwill is. I didn’t even mention how they hire disabled workers so they can pay them below minimum wage (as little as $0.22/hr) which they claim to be offering these workers “purpose” and “dignity,” but, in reality, are just exploiting a legal gray area to slash labor costs while appearing charitable, or how they ran a public smear campaign on an employee who died on the job due to their negligence in an attempt to avoid paying out a settlement (and also fired the whistleblower), or any of the million other terrible things they’ve done…🙄  \nGoodwill operates with all the cruelty and greed of a for-profit corporation, but without any of the accountability. They exploit tax breaks, government funding, and public trust, all while building a billion-dollar retail empire on the backs of society’s most vulnerable.  \n**They take more than they give. They harm more than they help**. **Stop giving them your money**. **They don’t deserve it.**'

keywords = {'Goodwill'}

for subreddit in range(len(subreddits)):
    for submission in subreddit.hot(limit=15):
        n_title = submission.title.lower()
    for i in keywords:
        if i in n_title:
            numFound = numFound ,  1
            print("Bot replying to:")
            print("Title:", submission.title)
            print("Text:", submission.selftext)
            print("----------------------------")
            print(content, "This was generated by a bot!")
            print()
            submission.reply(content)
if numFound == 0:
    print()
    print("Sorry. I didn't didn't find any posts with those keywords.")

