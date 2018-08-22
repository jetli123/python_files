# -*- coding: utf-8 -*-
__author__ = 'JetLi'
__version__ = '1.0.3_buid'
"""
    如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下
来，第二步就是解析该 HTML 页面，看看里面的内容到底是新闻、图
片还是视频。
"""
from HTMLParser import HTMLParser
# from htmlentitydefs import name2codepoint
import re


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print('data')

    def handle_comment(self, data):
        print('<!-- -->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

parser = MyHTMLParser()
# parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')
with open('G:\\PyCharm\\untitled\\abc.txt', 'w+') as f:
    f.write(parser.feed('''
<!doctype html>

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <link rel="prefetch" href="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js">

    <meta name="application-name" content="Python.org">
    <meta name="msapplication-tooltip" content="The official home of the Python Programming Language">
    <meta name="apple-mobile-web-app-title" content="Python.org">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="HandheldFriendly" content="True">
    <meta name="format-detection" content="telephone=no">
    <meta http-equiv="cleartype" content="on">
    <meta http-equiv="imagetoolbar" content="false">

    <script src="/static/js/libs/modernizr.js"></script>

    <link href="/static/stylesheets/style.css" rel="stylesheet" type="text/css" title="default" />
    <link href="/static/stylesheets/mq.css" rel="stylesheet" type="text/css" media="not print, braille, embossed, speech, tty" />


    <!--[if (lte IE 8)&(!IEMobile)]>
    <link href="/static/stylesheets/no-mq.css" rel="stylesheet" type="text/css" media="screen" />


    <![endif]-->


    <link rel="icon" type="image/x-icon" href="/static/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/static/apple-touch-icon-144x144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/static/apple-touch-icon-114x114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/static/apple-touch-icon-72x72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="/static/apple-touch-icon-precomposed.png">
    <link rel="apple-touch-icon" href="/static/apple-touch-icon-precomposed.png">


    <meta name="msapplication-TileImage" content="/static/metro-icon-144x144-precomposed.png"><!-- white shape -->
    <meta name="msapplication-TileColor" content="#3673a5"><!-- python blue -->
    <meta name="msapplication-navbutton-color" content="#3673a5">

    <title>Our Events | Python.org</title>

    <meta name="description" content="The official home of the Python Programming Language">
    <meta name="keywords" content="Python programming language object oriented web free open source software license documentation download community">


    <meta property="og:type" content="website">
    <meta property="og:site_name" content="Python.org">
    <meta property="og:title" content="Our Events">
    <meta property="og:description" content="The official home of the Python Programming Language">

    <meta property="og:image" content="https://www.python.org/static/opengraph-icon-200x200.png">
    <meta property="og:image:secure_url" content="https://www.python.org/static/opengraph-icon-200x200.png">

    <meta property="og:url" content="https://www.python.org/events/python-events/">

    <link rel="author" href="/static/humans.txt">

    <link rel="alternate" type="application/rss+xml" title="Python Enhancement Proposals"
          href="https://www.python.org/dev/peps/peps.rss/">
    <link rel="alternate" type="application/rss+xml" title="Python Job Opportunities"
          href="https://www.python.org/jobs/feed/rss/">
    <link rel="alternate" type="application/rss+xml" title="Python Software Foundation News"
          href="https://feeds.feedburner.com/PythonSoftwareFoundationNews">
    <link rel="alternate" type="application/rss+xml" title="Python Insider"
          href="https://feeds.feedburner.com/PythonInsider">





<body class="python events default-page">

    <div id="touchnav-wrapper">

        <div id="nojs" class="do-not-print">
            <p><strong>Notice:</strong> While Javascript is not essential for this website, your interaction with the content will be limited. Please turn Javascript on for the full experience. </p>
        </div>

        <!--[if lt IE 8]>
        <div id="oldie-warning" class="do-not-print">
            <p><strong>Notice:</strong> Your browser is <em>ancient</em> and <a href="http://www.ie6countdown.com/">Microsoft agrees</a>. <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience a better web.</p>
        </div>
        <![endif]-->

        <!-- Sister Site Links -->
        <div id="top" class="top-bar do-not-print">

            <nav class="meta-navigation container" role="navigation">


                <div class="skip-link screen-reader-text">
                    <a href="#content" title="Skip to content">Skip to content</a>
                </div>


                <a id="close-python-network" class="jump-link" href="#python-network" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-down"><span>&#9660;</span></span> Close
                </a>



<ul class="menu" role="tree">

    <li class="python-meta ">
        <a href="/" title="The Python Programming Language" >Python</a>
    </li>

    <li class="psf-meta ">
        <a href="/psf-landing/" title="The Python Software Foundation" >PSF</a>
    </li>

    <li class="docs-meta ">
        <a href="https://docs.python.org" title="Python Documentation" >Docs</a>
    </li>

    <li class="pypi-meta ">
        <a href="https://pypi.python.org/" title="Python Package Index" >PyPI</a>
    </li>

    <li class="jobs-meta ">
        <a href="/jobs/" title="Python Job Board" >Jobs</a>
    </li>

    <li class="shop-meta ">
        <a href="/community/" title="Python Community" >Community</a>
    </li>

</ul>


                <a id="python-network" class="jump-link" href="#top" aria-hidden="true">
                    <span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> The Python Network
                </a>

            </nav>

        </div>

        <!-- Header elements -->
        <header class="main-header" role="banner">
            <div class="container">

                <h1 class="site-headline">
                    <a href="/"><img class="python-logo" src="/static/img/python-logo.png" alt="python&trade;"></a>
                </h1>

                <div class="options-bar do-not-print">


                    <a id="site-map-link" class="jump-to-menu" href="#site-map"><span class="menu-icon">&equiv;</span> Menu</a><form class="search-the-site" action="/search/" method="get">
                        <fieldset title="Search Python.org">

                            <span aria-hidden="true" class="icon-search"></span>

                            <label class="screen-reader-text" for="id-search-field">Search This Site</label>
                            <input id="id-search-field" name="q" type="search" role="textbox" class="search-field" placeholder="Search" value="" tabindex="1">

                            <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
                                GO
                            </button>


                            <!--[if IE]><input type="text" style="display: none;" disabled="disabled" size="1" tabindex="4"><![endif]-->

                        </fieldset>
                    </form><span class="breaker"></span><div class="adjust-font-size" aria-hidden="true">
                        <ul class="navigation menu" aria-label="Adjust Text Size on Page">
                            <li class="tier-1 last" aria-haspopup="true">
                                <a href="#" class="action-trigger"><strong><small>A</small> A</strong></a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a class="text-shrink" title="Make Text Smaller" href="javascript:;">Smaller</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a class="text-grow" title="Make Text Larger" href="javascript:;">Larger</a></li>
                                    <li class="tier-2 element-3" role="treeitem"><a class="text-reset" title="Reset any font size changes I have made" href="javascript:;">Reset</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><div class="winkwink-nudgenudge">
                        <ul class="navigation menu" aria-label="Social Media Navigation">
                            <li class="tier-1 last" aria-haspopup="true">
                                <a href="#" class="action-trigger">Socialize</a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a href="http://plus.google.com/+Python"><span aria-hidden="true" class="icon-google-plus"></span>Google+</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a href="http://www.facebook.com/pythonlang?fref=ts"><span aria-hidden="true" class="icon-facebook"></span>Facebook</a></li>
                                    <li class="tier-2 element-3" role="treeitem"><a href="http://twitter.com/ThePSF"><span aria-hidden="true" class="icon-twitter"></span>Twitter</a></li>
                                    <li class="tier-2 element-4" role="treeitem"><a href="/community/irc/"><span aria-hidden="true" class="icon-freenode"></span>Chat on IRC</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div><div class="account-signin">
                        <ul class="navigation menu" aria-label="Social Media Navigation">
                            <li class="tier-1 last" aria-haspopup="true">

                                <a href="/accounts/login/" title="Sign Up or Sign In to Python.org">Sign In</a>
                                <ul class="subnav menu">
                                    <li class="tier-2 element-1" role="treeitem"><a href="/accounts/signup/">Sign Up / Register</a></li>
                                    <li class="tier-2 element-2" role="treeitem"><a href="/accounts/login/">Sign In</a></li>
                                </ul>

                            </li>
                        </ul>
                    </div>

                </div><!-- end options-bar -->

                <nav id="mainnav" class="python-navigation main-navigation do-not-print" role="navigation">


<ul class="navigation menu" role="menubar" aria-label="Main Navigation">



    <li id="about" class="tier-1 element-1  " aria-haspopup="true">
        <a href="/about/" title="" class="">About</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>

</ul>


    </li>



    <li id="downloads" class="tier-1 element-2  " aria-haspopup="true">
        <a href="/downloads/" title="" class="">Downloads</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>

</ul>


    </li>



    <li id="documentation" class="tier-1 element-3  " aria-haspopup="true">
        <a href="/doc/" title="" class="">Documentation</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>

        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>

</ul>


    </li>



    <li id="community" class="tier-1 element-4  " aria-haspopup="true">
        <a href="/community/" title="" class="">Community</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>

        <li class="tier-2 element-9" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>

        <li class="tier-2 element-10" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>

        <li class="tier-2 element-11" role="treeitem"><a href="https://www.python.org/psf/codeofconduct/" title="">Code of Conduct</a></li>

</ul>


    </li>



    <li id="success-stories" class="tier-1 element-5  " aria-haspopup="true">
        <a href="/about/success/" title="success-stories" class="">Success Stories</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/success/#arts" title="">Arts</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/success/#business" title="">Business</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/success/#education" title="">Education</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/success/#engineering" title="">Engineering</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/about/success/#government" title="">Government</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="/about/success/#scientific" title="">Scientific</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/about/success/#software-development" title="">Software Development</a></li>

</ul>


    </li>



    <li id="news" class="tier-1 element-6  " aria-haspopup="true">
        <a href="/blogs/" title="News from around the Python world" class="">News</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>

</ul>


    </li>



    <li id="events" class="tier-1 element-7  " aria-haspopup="true">
        <a href="/events/" title="" class="">Events</a>



<ul class="subnav menu" role="menu" aria-hidden="true">

        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>

</ul>


    </li>





</ul>


                </nav>

                <div class="header-banner "> <!-- for optional "do-not-print" class -->



                </div>




             </div><!-- end .container -->
        </header>

        <div id="content" class="content-wrapper">
            <!-- Main Content Column -->
            <div class="container">

                <section class="main-content with-right-sidebar" role="main">









        <header class="article-header">
            <h3>from the Python Events Calendar</h3>
        </header>


        <div class="most-recent-events">
            <div class="shrubbery">
                <h2 class="widget-title"><span aria-hidden="true" class="icon-calendar"></span>Upcoming Events</h2>

                <p class="give-me-more"><a href="?page=2" title="More Events">More</a></p>

                <ul class="list-recent-events menu">

                    <li>
                        <h3 class="event-title"><a href="/events/python-events/641/">PythonCamp 2018 - Cologne</a></h3>
                        <p>


<time datetime="2018-04-07T00:00:00+00:00">07 April &ndash; 09 April <span class="say-no-more"> 2018</span></time>




                            <span class="event-location">GFU Cyrus AG, Am Grauen Stein 27, 51105 Köln, Germany</span>

                        </p>
                    </li>

                    <li>
                        <h3 class="event-title"><a href="/events/python-events/585/">PyCon IT 9</a></h3>
                        <p>


<time datetime="2018-04-19T00:00:00+00:00">19 April &ndash; 23 April <span class="say-no-more"> 2018</span></time>




                            <span class="event-location">Hotel Mediterraneo - Lungarno del Tempio, 44, 50121 Firenze FI, Italy</span>

                        </p>
                    </li>

                    <li>
                        <h3 class="event-title"><a href="/events/python-events/658/">PyDays Vienna</a></h3>
                        <p>


<time datetime="2018-05-04T00:00:00+00:00">04 May &ndash; 06 May <span class="say-no-more"> 2018</span></time>




                            <span class="event-location">FH Technikum Wien, Hoechstaedtplatz 6, Vienna, Austria</span>

                        </p>
                    </li>

                    <li>
                        <h3 class="event-title"><a href="/events/python-events/608/">GeoPython 2018</a></h3>
                        <p>


<time datetime="2018-05-07T00:00:00+00:00">07 May &ndash; 10 May <span class="say-no-more"> 2018</span></time>




                            <span class="event-location">Basel, Switzerland</span>

                        </p>
                    </li>

                    <li>
                        <h3 class="event-title"><a href="/events/python-events/592/">PyCon US 2018</a></h3>
                        <p>


<time datetime="2018-05-09T00:00:00+00:00">09 May &ndash; 18 May <span class="say-no-more"> 2018</span></time>




                            <span class="event-location">Cleveland, Ohio, USA</span>

                        </p>
                    </li>

                    <li>
                        <h3 class="event-title"><a href="/events/python-events/640/">DjangoCon Europe 2018</a></h3>
                        <p>


<time datetime="2018-05-23T00:00:00+00:00">23 May &ndash; 28 May <span class="say-no-more"> 2018</span></time>




                            <span class="event-location">Heidelberg, Germany</span>

                        </p>
                    </li>

                </ul>
            </div>


            <h3 class="widget-title just-missed">You just missed...</h3>
            <ul class="list-recent-events menu">

                <li>
                    <h3 class="event-title"><a href="/events/python-events/604/">PyCon SK 2018</a></h3>
                    <p>


<time datetime="2018-03-09T00:00:00+00:00">09 March &ndash; 12 March <span class="say-no-more"> 2018</span></time>




                        <span class="event-location">Bratislava, Slovakia</span>

                    </p>
                </li>

                <li>
                    <h3 class="event-title"><a href="/events/python-events/648/">PyCon PH 2018</a></h3>
                    <p>


<time datetime="2018-02-24T00:00:00+00:00">24 Feb. &ndash; 26 Feb. <span class="say-no-more"> 2018</span></time>




                        <span class="event-location">Makati City, Metro Manila, Philippines</span>

                    </p>
                </li>

            </ul>

        </div>


                </section>





    <aside class="right-sidebar" role="secondary">
        <div class="sidebar-widget subscribe-widget">
            <h2 class="widget-title">Python Event Subscriptions</h2>
            <p>Subscribe to Python Event Calendars:</p>
            <ul class="menu">


                <li><a href="https://www.google.com/calendar/ical/j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com/public/basic.ics"><span aria-hidden="true" class="icon-ical"></span>Events in iCal format</a></li>

            </ul>
            <h2 class="widget-title">Python Events Calendars</h2>

<br/>

<p>For Python events near you, please have a look at the <a href="http://lmorillas.github.io/python_events/"><b>Python events map</b></a>.</p>

<p>The Python events calendars are maintained by the <a href="https://wiki.python.org/moin/PythonEventsCalendar#Python_Calendar_Team">events calendar team</a>.</p>

<p>Please see the <a href="https://wiki.python.org/moin/PythonEventsCalendar">events calendar project page</a> for details on how to <a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event">submit events</a>, <a href="https://wiki.python.org/moin/PythonEventsCalendar#Available_Calendars">subscribe to the calendars</a>, get <a href="https://twitter.com/PythonEvents">Twitter feeds</a> or embed them.</p>

<p>Thank you.</p>


	    </div>





    </aside>



            </div><!-- end .container -->
        </div><!-- end #content .content-wrapper -->

        <!-- Footer and social media list -->
        <footer id="site-map" class="main-footer" role="contentinfo">
            <div class="main-footer-links">
                <div class="container">


                    <a id="back-to-top-1" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>



<ul class="sitemap navigation menu do-not-print" role="tree" id="container">

    <li class="tier-1 element-1">
        <a href="/about/" >About</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/apps/" title="">Applications</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/quotes/" title="">Quotes</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/gettingstarted/" title="">Getting Started</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/help/" title="">Help</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="http://brochure.getpython.info/" title="">Python Brochure</a></li>

</ul>


    </li>

    <li class="tier-1 element-2">
        <a href="/downloads/" >Downloads</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/downloads/" title="">All releases</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/downloads/source/" title="">Source code</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/downloads/windows/" title="">Windows</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/downloads/mac-osx/" title="">Mac OS X</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/download/other/" title="">Other Platforms</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="https://docs.python.org/3/license.html" title="">License</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/download/alternatives" title="">Alternative Implementations</a></li>

</ul>


    </li>

    <li class="tier-1 element-3">
        <a href="/doc/" >Documentation</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/doc/" title="">Docs</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/doc/av" title="">Audio/Visual Talks</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="https://wiki.python.org/moin/BeginnersGuide" title="">Beginner&#39;s Guide</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://docs.python.org/faq/" title="">FAQ</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="http://wiki.python.org/moin/Languages" title="">Non-English Docs</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="http://python.org/dev/peps/" title="">PEP Index</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="https://wiki.python.org/moin/PythonBooks" title="">Python Books</a></li>

        <li class="tier-2 element-9" role="treeitem"><a href="/doc/essays/" title="">Python Essays</a></li>

</ul>


    </li>

    <li class="tier-1 element-4">
        <a href="/community/" >Community</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/community/diversity/" title="">Diversity</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/community/lists/" title="">Mailing Lists</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/community/irc/" title="">IRC</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/community/forums/" title="">Forums</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/community/workshops/" title="">Python Conferences</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="/community/sigs/" title="">Special Interest Groups</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="https://wiki.python.org/moin/" title="">Python Wiki</a></li>

        <li class="tier-2 element-8" role="treeitem"><a href="/community/logos/" title="">Python Logo</a></li>

        <li class="tier-2 element-9" role="treeitem"><a href="/community/merchandise/" title="">Merchandise</a></li>

        <li class="tier-2 element-10" role="treeitem"><a href="/community/awards" title="">Community Awards</a></li>

        <li class="tier-2 element-11" role="treeitem"><a href="https://www.python.org/psf/codeofconduct/" title="">Code of Conduct</a></li>

</ul>


    </li>

    <li class="tier-1 element-5">
        <a href="/about/success/" title="success-stories">Success Stories</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/about/success/#arts" title="">Arts</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/about/success/#business" title="">Business</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/about/success/#education" title="">Education</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/about/success/#engineering" title="">Engineering</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="/about/success/#government" title="">Government</a></li>

        <li class="tier-2 element-6" role="treeitem"><a href="/about/success/#scientific" title="">Scientific</a></li>

        <li class="tier-2 element-7" role="treeitem"><a href="/about/success/#software-development" title="">Software Development</a></li>

</ul>


    </li>

    <li class="tier-1 element-6">
        <a href="/blogs/" title="News from around the Python world">News</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/blogs/" title="Python Insider Blog Posts">Python News</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="http://planetpython.org/" title="Planet Python">Community News</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="http://pyfound.blogspot.com/" title="PSF Blog">PSF News</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="http://pycon.blogspot.com/" title="PyCon Blog">PyCon News</a></li>

</ul>


    </li>

    <li class="tier-1 element-7">
        <a href="/events/" >Events</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="/events/python-events" title="">Python Events</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="/events/python-user-group/" title="">User Group Events</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="/events/python-events/past/" title="">Python Events Archive</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/events/python-user-group/past/" title="">User Group Events Archive</a></li>

        <li class="tier-2 element-5" role="treeitem"><a href="https://wiki.python.org/moin/PythonEventsCalendar#Submitting_an_Event" title="">Submit an Event</a></li>

</ul>


    </li>

    <li class="tier-1 element-8">
        <a href="/dev/" >Contributing</a>



<ul class="subnav menu">

        <li class="tier-2 element-1" role="treeitem"><a href="https://devguide.python.org/" title="">Developer&#39;s Guide</a></li>

        <li class="tier-2 element-2" role="treeitem"><a href="https://bugs.python.org/" title="">Issue Tracker</a></li>

        <li class="tier-2 element-3" role="treeitem"><a href="https://mail.python.org/mailman/listinfo/python-dev" title="">python-dev list</a></li>

        <li class="tier-2 element-4" role="treeitem"><a href="/dev/core-mentorship/" title="">Core Mentorship</a></li>

</ul>


    </li>

</ul>


                    <a id="back-to-top-2" class="jump-link" href="#python-network"><span aria-hidden="true" class="icon-arrow-up"><span>&#9650;</span></span> Back to Top</a>


                </div><!-- end .container -->
            </div> <!-- end .main-footer-links -->

            <div class="site-base">
                <div class="container">

                    <ul class="footer-links navigation menu do-not-print" role="tree">
                        <li class="tier-1 element-1"><a href="/about/help/">Help &amp; <span class="say-no-more">General</span> Contact</a></li>
                        <li class="tier-1 element-2"><a href="/community/diversity/">Diversity <span class="say-no-more">Initiatives</span></a></li>
                        <li class="tier-1 element-3"><a href="https://github.com/python/pythondotorg/issues">Submit Website Bug</a></li>
                        <li class="tier-1 element-4">
                            <a href="https://status.python.org/">Status <span class="python-status-indicator-default" id="python-status-indicator"></span></a>
                        </li>
                    </ul>

                    <div class="copyright">
                        <p><small>
                            <span class="pre">Copyright &copy;2001-2018.</span>
                            &nbsp;<span class="pre"><a href="/psf-landing/">Python Software Foundation</a></span>
                            &nbsp;<span class="pre"><a href="/about/legal/">Legal Statements</a></span>
                            &nbsp;<span class="pre"><a href="/privacy/">Privacy Policy</a></span>
                            &nbsp;<span class="pre"><a href="/psf/sponsorship/sponsors/">Powered by Rackspace</a></span>
                        </small></p>
                    </div>

                </div><!-- end .container -->
            </div><!-- end .site-base -->

        </footer>

    </div><!-- end #touchnav-wrapper -->


    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="/static/js/libs/jquery-1.8.2.min.js"><\/script>')</script>

    <script src="/static/js/libs/masonry.pkgd.min.js"></script>

    <script type="text/javascript" src="/static/js/main-min.js" charset="utf-8"></script>


    <!--[if lte IE 7]>
    <script type="text/javascript" src="/static/js/plugins/IE8-min.js" charset="utf-8"></script>

    <![endif]--
    <!--[if lte IE 8]>
    <script type="text/javascript" src="/static/js/plugins/getComputedStyle-min.js" charset="utf-8"></script
    <![endif]-->
</body>
</html>'''))

# fil = re.compile(r'^(&#[0-9]{1,10}$)')
# fil.match(r'G:\\PyCharm\\untitled\\abc.txt').group()
# print fil