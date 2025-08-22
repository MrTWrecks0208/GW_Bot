import praw
import time

# --- CONFIGURATION ---
userAgent = 'GWBot'
clientId = 'pnsZpSjLJ9_2Bt-sxY5JmQ'
secret = 'amqJtcQeq2TYyNxDy_1_czvsbdlyNg'
username = 'mrtwrecksDEV'
password = 'R7%y6GTCvnr3&hnP'

reddit = praw.Reddit(
    user_agent=userAgent,
    client_id=clientId,
    client_secret=secret,
    username=username,
)

subreddits = ["flipping", "thesidehustle", "sidehustle", "houston", "thrift", "pics", "thriftstorehauls", 'millenials', 'xennials', 'genz', 'thriftstorefinds', 'thriftgift', 'gamecollecting', 'frugal', 'frugal_jerk', 'thriftedfasion', 'cd_collectors', 'dvdcollection', 'thrifty', 'savingmoney', 'goodwill_finds', 'sneakers', 'whatisthisthing', 'cassetteculture', 'thriftstorefasion', 'repaintings', 'vinyl', 'goodwillbins', 'thriftpaintings', 'thriftflip', 'frugalwrist', 'verycheap', 'vintageaudio', 'gaming', 'streetwear', 'mildlyinteresting', 'funny', 'barbie', 'antiques', 'analogcommunity', 'bookhaul', 'glasscollecting', 'sewing', 'depop', 'vintagefashion', 'whatisthis', 'crochet', 'vintage', 'vintagetees', 'starwars', 'bargainbinvinyl', 'thredup', 'wtfgaragesale', 'donate', 'charitabledonations', 'charity', 'nonprofit', 'vinted', 'retail', 'flippingfinds', 'reselling', 'teenagers', 'resellprofits', 'askreddit', 'shoppingaddiction', 'antiwork', 'anticonsumption', 'frugalshopping', 'resell']

content = 'Goodwill is a deeply exploitative organization, top to bottom. Their entire business model is built on taking advantage of vulnerable people. They use their career centers to funnel individuals (often those with criminal records) to staff their stores, where they’re overworked, underpaid, and treated like shit. Many of these workers have limited options available to them and can’t just go get another job. They are stuck at Goodwill. Goodwill knows this and uses it to their advantage whenever possible.\n\n'
'Goodwill claims that ~89-93 cents of every dollar (varies by location) spent in their stores goes toward vocational training and employment services. That’s a complete lie. All their programs are funded by/through government grants. Look at their Form 990 filings on ProPublica. At the location where I worked, only about 9 cents of every dollar actually went to those services. The rest went toward executive compensation and profit-driven operations under the guise of charity. Goodwill does next to nothing to actually help people.\n\n'
'In addition to not helping the public and/or community, Goodwill doesn’t even help their own employees! After a major hurricane in which many employees were without power and some lost their homes/everything, etc. Goodwill told us if we needed anything, we should contact Workforce Solutions. Goodwill offered zero assistance. They also required us to go into the office or face termination. Their warehouses and offices are often filled with OSHA violations, requiring employees to stay at work at times when there is no running water or bathroom available, or when there is no A/C. Hell, my location tried to force us into an office that they knew was infested with bedbugs and threatened to terminate us if we didn’t go in. \n\n'
'Goodwill management loves to threaten employees. It’s their go-to for anything and everything. So, let’s say you are actually terminated by Goodwill… good luck getting unemployment! Goodwill fights every single claim tooth and nail to make sure the terminated employee does not get a single dime in unemployment benefits. If you happen to win and are awarded benefits, they will submit as many appeals as they are legally allowed to. They have no problem kicking you while you’re down and out. They love it. Yes, they’re this pathetic.\n\n'
'This doesn’t even scratch the surface of how shitty Goodwill is. I didn’t even mention how they hire disabled workers so they can pay them below minimum wage (as little as $0.22/hr) which they’re able to do because of an archaic law that is only still on the books because Goodwill executives lobby the government to keep the law on the books, or how they ran a public smear campaign on an employee who died on the job due to their negligence in an attempt to sway public opinion and avoid paying out a settlement to the family (They also fired the whistleblower btw), or any of the million other terrible things they’ve done…🙄\n\n'
'They give little back to the community and operate with the same greed you’d expect from a for-profit corporation—just without the accountability. Stop giving them your money. They don’t deserve it.'

keywords = {'goodwill'}

sleep_time = 30  # seconds between checks to avoid rate limits

# Keep track of items we've replied to so we don't duplicate
already_replied = set()

def process_comment(comment):
    # Ignore our own comments
    if str(comment.author).lower() == username.lower():
        return
    # Check keyword
    if keywords.lower() in comment.body.lower():
        if comment.id not in already_replied:
            print(f"Replying to comment {comment.id} in r/{comment.subreddit}")
            comment.reply(content)
            already_replied.add(comment.id)

def process_submission(submission):
    # Ignore our own posts
    if str(submission.author).lower() == username.lower():
        return
    # Check keyword in title or selftext
    text_to_check = submission.title + " " + submission.selftext
    if keywords.lower() in text_to_check.lower():
        if submission.id not in already_replied:
            print(f"Replying to submission {submission.id} in r/{submission.subreddit}")
            submission.reply(content)
            already_replied.add(submission.id)


def main():
    while True:
        try:
            for sub in subreddits:
                subreddit = reddit.subreddit(sub)

                # Process new submissions
                for submission in subreddit.new(limit=20):
                    process_submission(submission)

                # Process new comments
                for comment in subreddit.comments(limit=20):
                    process_comment(comment)

            time.sleep(sleep_time)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)  # wait a minute if there's an error (network, rate limit, etc.)


if __name__ == "__main__":
    main()
