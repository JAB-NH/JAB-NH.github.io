import os

# Define the shared layout
LAYOUT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | JAMES * JIMMY * JIDO</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        'brand-peach': '#FAD0A1',
                        'brand-peach-light': '#FDF3E7',
                        'brand-teal': '#319795',
                        'brand-dark': '#2d3748'
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #fcfaf8; color: #2d3748; }}
        .nav-link {{ color: #4a5568; transition: color 0.2s; }}
        .nav-link:hover {{ color: #319795; }}
        .active {{ color: #319795; font-weight: bold; border-bottom: 3px solid #319795; padding-bottom: 2px; }}
        details > summary {{ list-style: none; cursor: pointer; outline: none; }}
        details > summary::-webkit-details-marker {{ display: none; }}
        details[open] summary svg {{ transform: rotate(180deg); }}
    </style>
</head>
<body class="flex flex-col min-h-screen">
    <!-- Navbar -->
    <nav class="bg-brand-peach shadow-md border-b border-orange-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-20">
                <div class="flex items-center">
                    <a href="index.html" class="flex-shrink-0 flex items-center text-gray-900 font-extrabold text-2xl tracking-wider">
                        JAMES * JIMMY * JIDO
                    </a>
                    <div class="hidden md:ml-8 md:flex md:space-x-8 overflow-x-auto">
                        <a href="index.html" class="nav-link inline-flex items-center px-1 pt-1 text-base font-semibold {nav_home}">Home</a>
                        <a href="why.html" class="nav-link inline-flex items-center px-1 pt-1 text-base font-semibold {nav_why}">Why a Website</a>
                        <a href="who.html" class="nav-link inline-flex items-center px-1 pt-1 text-base font-semibold {nav_who}">Who Am I</a>
                        <a href="musings.html" class="nav-link inline-flex items-center px-1 pt-1 text-base font-semibold {nav_musings}">Musings</a>
                        <a href="personal.html" class="nav-link inline-flex items-center px-1 pt-1 text-base font-semibold {nav_personal}">Personal</a>
                        <a href="tunes.html" class="nav-link inline-flex items-center px-1 pt-1 text-base font-semibold {nav_tunes}">Tunes</a>
                        <a href="about.html" class="nav-link inline-flex items-center px-1 pt-1 text-base font-semibold {nav_about}">About</a>
                    </div>
                </div>
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-grow w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        {content}
    </main>

    <!-- Footer -->
    <footer class="bg-brand-peach border-t border-orange-200 text-gray-800 py-8 mt-12">
        <div class="max-w-7xl mx-auto px-4 text-center font-medium">
            <p>&copy; 2026 James Allen Bates. All Rights Reserved.</p>
        </div>
    </footer>
</body>
</html>
"""

# Pages content definitions
pages = {}

pages['index.html'] = {
    'title': 'Home',
    'nav': 'nav_home',
    'content': """
        <div class="bg-brand-peach rounded-xl shadow-lg overflow-hidden mb-12 border border-orange-200">
            <div class="md:flex">
                <div class="md:w-3/5 px-8 py-16 text-left flex flex-col justify-center">
                    <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight mb-4 text-gray-900">A Personal Journey</h1>
                    <p class="text-xl md:text-2xl font-medium italic text-gray-800 max-w-3xl">
                        (Just like home movies, but you get to choose when you've had enough!)
                    </p>
                </div>
                <div class="md:w-2/5 hidden md:block">
                    <img src="assets/img/philosopher1.png" alt="Philosopher" class="w-full h-full object-cover opacity-90 mix-blend-multiply">
                </div>
            </div>
        </div>

        <div class="max-w-4xl mx-auto bg-white rounded-lg shadow-sm border border-gray-100 p-8 mb-12">
            <h2 class="text-3xl font-bold text-gray-900 mb-6 border-b pb-2">Welcome & Navigation Guide</h2>
            
            <div class="md:flex mb-8 items-start">
                <div class="md:w-2/3 md:pr-8">
                    <p class="text-lg text-gray-700 leading-relaxed mb-6">
                        Welcome to my personal corner of the web! This site serves as a digital repository of my experiences, thoughts, original music, and family history. I've designed it primarily as a legacy archive for my step-grandchildren and family, but anyone curious is welcome to explore.
                    </p>
                </div>
                <div class="md:w-1/3 mb-6 md:mb-0">
                    <img src="assets/img/writingdesk2better.png" alt="Writing Desk" class="rounded-lg shadow-sm w-full border border-gray-200">
                </div>
            </div>

            <h3 class="text-2xl font-bold text-brand-teal mb-6">Explore the Site:</h3>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <a href="why.html" class="block p-6 bg-brand-peach-light rounded-lg border border-orange-100 hover:shadow-lg transition">
                    <h4 class="text-xl font-bold text-gray-900 mb-2">Why a Website?</h4>
                    <p class="text-gray-700">Why share contentious views publicly? Vulnerability, future references, and digital learning.</p>
                </a>
                <a href="who.html" class="block p-6 bg-brand-peach-light rounded-lg border border-orange-100 hover:shadow-lg transition">
                    <h4 class="text-xl font-bold text-gray-900 mb-2">Who Am I?</h4>
                    <p class="text-gray-700">A dive into my history: family pictures (1955+), genealogy records, and my life-tracking spreadsheet.</p>
                </a>
                <a href="musings.html" class="block p-6 bg-brand-peach-light rounded-lg border border-orange-100 hover:shadow-lg transition">
                    <h4 class="text-xl font-bold text-gray-900 mb-2">Musings</h4>
                    <p class="text-gray-700">My books: <em>History of the Universe</em> and <em>Global Communication</em>. Available as PDFs or AI podcasts!</p>
                </a>
                <a href="personal.html" class="block p-6 bg-brand-peach-light rounded-lg border border-orange-100 hover:shadow-lg transition">
                    <h4 class="text-xl font-bold text-gray-900 mb-2">Personal</h4>
                    <p class="text-gray-700">Crazy real-life stories (parachuting, plane crashes, TV game shows) and my core beliefs.</p>
                </a>
                <a href="tunes.html" class="block p-6 bg-brand-peach-light rounded-lg border border-orange-100 hover:shadow-lg transition">
                    <h4 class="text-xl font-bold text-gray-900 mb-2">Tunes</h4>
                    <p class="text-gray-700">Original guitar tracks recorded over a 35-year span, along with the personal stories behind them.</p>
                </a>
                <a href="about.html" class="block p-6 bg-brand-peach-light rounded-lg border border-orange-100 hover:shadow-lg transition">
                    <h4 class="text-xl font-bold text-gray-900 mb-2">About</h4>
                    <p class="text-gray-700">Meet Norma (44+ years together!) and learn the meaning behind my three names: James, Jimmy, and Jido.</p>
                </a>
            </div>
        </div>
    """
}

pages['why.html'] = {
    'title': 'Why a Website',
    'nav': 'nav_why',
    'content': """
        <div class="max-w-4xl mx-auto">
            <h1 class="text-4xl font-bold text-gray-900 mb-8 border-b pb-4">Why a Website?</h1>
            <p class="text-xl text-gray-700 leading-relaxed mb-8">
                Is it worth the time and effort to maintain a personal website in the 21st century? For me, the answer is a resounding yes. It boils down to four main motivations:
            </p>

            <div class="space-y-4">
                <!-- Collapsible 1 -->
                <details class="group bg-white rounded-lg shadow">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none p-6 text-xl text-gray-900">
                        <span>1. Vulnerability & Commitment</span>
                        <span class="transition group-open:rotate-180">
                            <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-6 pt-0 text-gray-700 leading-relaxed border-t mt-4 pt-4">
                        <p class="mb-4"><strong>Standing by your beliefs publicly.</strong></p>
                        <p class="mb-4">It is one thing to hold a contentious point of view privately. It is another thing to anonymously post a contentious point of view on the internet.</p>
                        <p>But it takes true <strong>vulnerability and commitment</strong> to publicly express a contentious point of view under your own name, where you can be held accountable for it. This site is a commitment to sharing what I believe, openly and honestly.</p>
                    </div>
                </details>

                <!-- Collapsible 2 -->
                <details class="group bg-white rounded-lg shadow">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none p-6 text-xl text-gray-900">
                        <span>2. Future Reference</span>
                        <span class="transition group-open:rotate-180">
                            <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-6 pt-0 text-gray-700 leading-relaxed border-t mt-4 pt-4">
                        <p class="mb-4"><strong>A digital legacy for those who come after.</strong></p>
                        <p class="mb-4">I have finally reached an age where I would love to know all kinds of things about my parents and grandparents. However, I find that they are all gone, and I missed out on that opportunity.</p>
                        <p>This realization got me thinking: perhaps a collection of odds and ends from my own personal experiences might eventually be of some interest to someone else someday. This website is the result of that process. It is a repository for my children, grandchildren, and friends to explore whenever they want to learn a bit more about where they came from.</p>
                    </div>
                </details>

                <!-- Collapsible 3 -->
                <details class="group bg-white rounded-lg shadow">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none p-6 text-xl text-gray-900">
                        <span>3. Entertainment</span>
                        <span class="transition group-open:rotate-180">
                            <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-6 pt-0 text-gray-700 leading-relaxed border-t mt-4 pt-4">
                        <p class="mb-4"><strong>The joy of building and experimenting.</strong></p>
                        <p class="mb-4">Beyond the personal archives, how much fun has this been? Building this site and experimenting with the web has been an incredible playground. Over the years, I have built interactive games, image recognition systems, and even rudimentary neural networks to garner a basic understanding of how these new technological environments will impact our future.</p>
                        <p>It has been an absolute blast, and I know far more now about the future of software and technology than I ever imagined I would.</p>
                    </div>
                </details>

                <!-- Collapsible 4 -->
                <details class="group bg-white rounded-lg shadow">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none p-6 text-xl text-gray-900">
                        <span>4. Demonstration & Education</span>
                        <span class="transition group-open:rotate-180">
                            <svg fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-6 pt-0 text-gray-700 leading-relaxed border-t mt-4 pt-4">
                        <p class="mb-4"><strong>Keeping pace with an accelerating digital world.</strong></p>
                        <p class="mb-4">The pace of internet learning is exploding. I often feel that as quickly as I learn a new skill, the very next week some new capability is already required.</p>
                        <p class="mb-4">Modern tools have changed the game. Today, creating your own website couldn't be easier. It is all drag-and-drop, with no coding required. Everybody has something worth saving and sharing: pictures, home videos, MP3s, or PDFs.</p>
                        <p>My hope is to demonstrate that anyone can build a modern web presence. By letting others provide the layout and design frameworks, we can concentrate entirely on the actual content and learn new digital skills along the way.</p>
                    </div>
                </details>
            </div>
        </div>
    """
}

pages['who.html'] = {
    'title': 'Who Am I',
    'nav': 'nav_who',
    'content': """
        <div class="max-w-5xl mx-auto">
            <h1 class="text-4xl font-bold text-gray-900 mb-8 border-b pb-4">Who Am I?</h1>
            
            <div class="bg-white rounded-lg shadow p-8 mb-10">
                <p class="text-xl text-gray-700 leading-relaxed mb-6">
                    To different people and in different parts of my life, I have been known by three distinct names: <strong>James</strong>, <strong>Jimmy</strong>, and <strong>Jido</strong>. Each represents a different side of my journey:
                </p>
                <ul class="list-disc pl-6 space-y-4 text-lg text-gray-700 mb-8">
                    <li><strong>James:</strong> The official side. The name on my passport, financial documents, tax forms, and professional business correspondence.</li>
                    <li><strong>Jimmy:</strong> The social and creative side. A term of endearment from work colleagues and friends. Jimmy is the guy who is out there living the dream, playing guitar, and enjoying life.</li>
                    <li><strong>Jido:</strong> The family side. This is the Arabic name for a grandfather, which is how my step-grandchildren address me. It represents my role as a guardian, looking out for their future and keeping these records for them.</li>
                </ul>
                <p class="text-gray-600 italic">You can read the full story behind these names and my partner Norma on the <a href="about.html" class="text-brand-teal hover:underline">About Us</a> page.</p>
            </div>

            <h2 class="text-3xl font-bold text-gray-900 mb-6">Explore My Story</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <a href="pictures.html" class="block p-8 bg-brand-dark text-white rounded-xl shadow-lg hover:bg-gray-800 transition transform hover:-translate-y-1">
                    <h3 class="text-2xl font-bold mb-3">Family Pictures</h3>
                    <p class="text-gray-300">Browse vintage photos of my childhood, parents, and grandparents dating back to the 1950s.</p>
                </a>
                
                <a href="genealogy.html" class="block p-8 bg-brand-teal text-white rounded-xl shadow-lg hover:bg-teal-700 transition transform hover:-translate-y-1">
                    <h3 class="text-2xl font-bold mb-3">Genealogy</h3>
                    <p class="text-teal-100">View our family lineage documentation and download the complete family tree.</p>
                </a>
                
                <a href="lifeline.html" class="block p-8 bg-white border-2 border-brand-teal text-brand-teal rounded-xl shadow-lg hover:bg-teal-50 transition transform hover:-translate-y-1">
                    <h3 class="text-2xl font-bold mb-3">My Lifeline</h3>
                    <p class="text-gray-600">Learn about my personal project to track my life milestones, jobs, and cars year-by-year.</p>
                </a>
            </div>
        </div>
    """
}

pages['pictures.html'] = {
    'title': 'Family Pictures',
    'nav': 'nav_who',
    'content': """
        <div class="max-w-4xl mx-auto">
            <div class="mb-8 flex items-center justify-between border-b pb-4">
                <h1 class="text-4xl font-bold text-gray-900">Family Pictures</h1>
                <a href="who.html" class="text-brand-teal hover:underline">&larr; Back to Who Am I</a>
            </div>
            <p class="text-xl text-gray-700 leading-relaxed mb-10">A collection of historical family photographs spanning three generations.</p>

            <div class="space-y-12">
                <div class="bg-white rounded-lg shadow overflow-hidden">
                    <div class="p-8 md:flex">
                        <div class="md:w-1/2 flex items-center justify-center bg-gray-100 rounded mb-6 md:mb-0 md:mr-8 overflow-hidden">
                            <img src="assets/img/BatesFamily/Judy%20Nancy%20Jimmy%20850%20Hotham.jpg" alt="The Kids" class="max-w-full h-auto object-cover">
                        </div>
                        <div class="md:w-1/2 flex flex-col justify-center">
                            <h2 class="text-2xl font-bold text-gray-900 mb-2">The Kids</h2>
                            <p class="text-gray-600 mb-1"><strong>Location:</strong> 850 Hotham Street, Esquimalt (Naden), BC</p>
                            <p class="text-gray-600 mb-4"><strong>Date:</strong> Circa 1955</p>
                            <p class="text-gray-800 font-semibold mb-2">Left to Right:</p>
                            <ul class="list-disc pl-5 text-gray-700">
                                <li>Nancy Elizabeth</li>
                                <li>James Allen</li>
                                <li>Judith Ellen</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-lg shadow overflow-hidden">
                    <div class="p-8 md:flex">
                        <div class="md:w-1/2 flex items-center justify-center bg-gray-100 rounded mb-6 md:mb-0 md:mr-8 overflow-hidden">
                            <img src="assets/img/BatesFamily/BatesFamily1952.jpg" alt="The Parents" class="max-w-full h-auto object-cover">
                        </div>
                        <div class="md:w-1/2 flex flex-col justify-center">
                            <h2 class="text-2xl font-bold text-gray-900 mb-2">The Parents</h2>
                            <p class="text-gray-600 mb-1"><strong>Location:</strong> Qualicum Beach, BC</p>
                            <p class="text-gray-600 mb-4"><strong>Date:</strong> Circa 1955</p>
                            <p class="text-gray-800 font-semibold mb-2">Names:</p>
                            <ul class="list-disc pl-5 text-gray-700">
                                <li>Peter James Bates</li>
                                <li>Gwenyth Irene Bates</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="bg-white rounded-lg shadow overflow-hidden">
                    <div class="p-8 md:flex">
                        <div class="md:w-1/2 flex items-center justify-center bg-gray-100 rounded mb-6 md:mb-0 md:mr-8 overflow-hidden">
                            <img src="assets/img/BatesFamily/Woodstock001.jpg" alt="The Grandparents" class="max-w-full h-auto object-cover">
                        </div>
                        <div class="md:w-1/2 flex flex-col justify-center">
                            <h2 class="text-2xl font-bold text-gray-900 mb-2">The Grandparents & Family</h2>
                            <p class="text-gray-600 mb-1"><strong>Location:</strong> 683 Brant Street, Woodstock, Ontario</p>
                            <p class="text-gray-600 mb-4"><strong>Date:</strong> Circa 1962</p>
                            <p class="text-gray-800 font-semibold mb-2">Left to Right:</p>
                            <ul class="list-disc pl-5 text-gray-700">
                                <li>Jimmy (young James)</li>
                                <li>Edna Wilson</li>
                                <li>Malcolm & Susan Allen</li>
                                <li>Frederick & Lucille Knapp</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    """
}

pages['genealogy.html'] = {
    'title': 'Genealogy',
    'nav': 'nav_who',
    'content': """
        <div class="max-w-4xl mx-auto">
            <div class="mb-8 flex items-center justify-between border-b pb-4">
                <h1 class="text-4xl font-bold text-gray-900">Genealogy</h1>
                <a href="who.html" class="text-brand-teal hover:underline">&larr; Back to Who Am I</a>
            </div>
            
            <div class="bg-white rounded-lg shadow p-8 mb-8">
                <p class="text-xl text-gray-700 leading-relaxed mb-8">
                    This page contains historical lineage records tracking the origins and branches of the Bates family tree. For those researching our family history or looking to browse the complete lineage, please download the document below.
                </p>
                
                <div class="bg-gray-50 border rounded-lg p-6 flex flex-col md:flex-row items-center justify-between">
                    <div class="mb-4 md:mb-0">
                        <h3 class="text-2xl font-bold text-gray-900">Bates Family Lineage</h3>
                        <p class="text-gray-600 mt-1">Detailed lineage tracking names, births, marriages, and movements.</p>
                        <p class="text-sm text-gray-500 mt-2">Format: PDF Document</p>
                    </div>
                    <a href="assets/docs/Bates_Lineage.pdf" class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-brand-teal hover:bg-teal-700 focus:outline-none transition">
                        <svg class="-ml-1 mr-3 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
                        </svg>
                        Download PDF
                    </a>
                </div>
            </div>
        </div>
    """
}

pages['lifeline.html'] = {
    'title': 'Lifeline',
    'nav': 'nav_who',
    'content': """
        <div class="max-w-4xl mx-auto">
            <div class="mb-8 flex items-center justify-between border-b pb-4">
                <h1 class="text-4xl font-bold text-gray-900">My Lifeline</h1>
                <a href="who.html" class="text-brand-teal hover:underline">&larr; Back to Who Am I</a>
            </div>
            
            <div class="bg-white rounded-lg shadow p-8 mb-10">
                <h2 class="text-2xl font-semibold text-gray-900 mb-4">Tracking a lifetime, year by year.</h2>
                <p class="text-lg text-gray-700 leading-relaxed mb-4">
                    This spreadsheet project might seem a bit detailed to most, but it has proven incredibly useful. I still refer to it many times when I need to confirm when a specific event took place—like what grade I was in when a childhood bully confronted me in 1968 (grade 3, as it turns out!). Keeping track of those details becomes harder as the years go by.
                </p>
                
                <h3 class="text-xl font-bold text-gray-900 mt-8 mb-3">How it Started</h3>
                <p class="text-lg text-gray-700 leading-relaxed mb-4">
                    I began by simply tracking my birthday year-by-year to figure out exactly how old I was in each school grade. This exercise surprised me and led to a personal crusade to confirm dates. What followed was an outstanding adventure:
                </p>
                <ul class="list-disc pl-6 space-y-2 text-lg text-gray-700 mb-6">
                    <li>I recovered digital reproductions of class photographs from the <strong>1969 Ottawa Teacher's College Archive</strong>.</li>
                    <li>I accumulated a complete digital edition of every single high school yearbook from my years of attendance (a claim not many high schoolers can make!).</li>
                </ul>

                <p class="text-lg text-gray-700 leading-relaxed mb-8">
                    Eventually, I expanded the sheet to track where I was working, where I was living, the car I was driving, and special milestones. It has been handy on more than a few occasions, and I hope it serves as a helpful template if you ever want to track your own milestones.
                </p>

                <h3 class="text-2xl font-bold text-gray-900 mb-4 border-t pt-6">Summary of what is tracked</h3>
                <div class="overflow-x-auto mb-8">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Category</th>
                                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Example Entry</th>
                                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Purpose</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-200">
                            <tr>
                                <td class="px-6 py-4 whitespace-nowrap font-medium text-gray-900">Year / Age</td>
                                <td class="px-6 py-4 whitespace-nowrap text-gray-500">1969 (Age 13)</td>
                                <td class="px-6 py-4 text-gray-500">Keep chronological alignment.</td>
                            </tr>
                            <tr>
                                <td class="px-6 py-4 whitespace-nowrap font-medium text-gray-900">Location</td>
                                <td class="px-6 py-4 whitespace-nowrap text-gray-500">Ottawa, ON</td>
                                <td class="px-6 py-4 text-gray-500">Track residences and moves.</td>
                            </tr>
                            <tr>
                                <td class="px-6 py-4 whitespace-nowrap font-medium text-gray-900">Education / Work</td>
                                <td class="px-6 py-4 whitespace-nowrap text-gray-500">Algonquin College</td>
                                <td class="px-6 py-4 text-gray-500">Track school years and job changes.</td>
                            </tr>
                            <tr>
                                <td class="px-6 py-4 whitespace-nowrap font-medium text-gray-900">Vehicles</td>
                                <td class="px-6 py-4 whitespace-nowrap text-gray-500">1971 Toyota Corolla</td>
                                <td class="px-6 py-4 text-gray-500">Keep record of cars driven.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="bg-brand-peach-light border border-orange-200 rounded-lg p-6 text-center">
                    <a href="https://docs.google.com/spreadsheets/d/14q-pBpJeUyv3VrEsOVL_4q5zdOtVsQgmw0LyFxGPW9Y/edit?gid=0#gid=0" target="_blank" class="inline-flex items-center px-6 py-3 border border-transparent text-lg font-medium rounded-md shadow-sm text-white bg-brand-teal hover:bg-teal-700 focus:outline-none transition">
                        <svg class="-ml-1 mr-3 h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                        </svg>
                        View Jim's Public Lifeline (Google Sheets)
                    </a>
                    <p class="text-sm text-gray-500 mt-3">Clicking will open the spreadsheet in a new tab.</p>
                </div>
            </div>
        </div>
    """
}

pages['musings.html'] = {
    'title': 'Musings',
    'nav': 'nav_musings',
    'content': """
        <div class="max-w-5xl mx-auto">
            <h1 class="text-4xl font-bold text-gray-900 mb-8 border-b pb-4">Musings</h1>
            
            <div class="bg-white rounded-lg shadow-md p-8 mb-12 border-l-4 border-brand-teal">
                <p class="text-2xl text-gray-700 italic leading-relaxed mb-4">
                    "I have always believed that the best way to figure out if I really understand something or not is to write about it."
                </p>
                <p class="text-lg text-gray-600">
                    Welcome to my musings. Writing has always been my favorite method for processing complex topics and consolidating what I learn.
                </p>
            </div>

            <p class="text-xl text-gray-800 mb-6 font-medium">For each subject below, I invite you to explore the content through two distinct pathways:</p>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
                <div class="bg-gray-50 rounded-lg p-6 border">
                    <h3 class="text-xl font-bold text-gray-900 mb-2 flex items-center">
                        <span class="bg-brand-dark text-white rounded-full w-8 h-8 flex items-center justify-center mr-3 text-sm">1</span>
                        The Written Word
                    </h3>
                    <p class="text-gray-600">Read the complete, illustrated, and fully researched traditional PDF manuscripts.</p>
                </div>
                <div class="bg-gray-50 rounded-lg p-6 border">
                    <h3 class="text-xl font-bold text-gray-900 mb-2 flex items-center">
                        <span class="bg-brand-teal text-white rounded-full w-8 h-8 flex items-center justify-center mr-3 text-sm">2</span>
                        The AI Podcast
                    </h3>
                    <p class="text-gray-600">Listen to a lively conversational podcast, generated by AI, which summarizes and debates the core themes.</p>
                </div>
            </div>

            <h2 class="text-3xl font-bold text-gray-900 mb-8">Choose Your Adventure</h2>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
                <!-- Book 1 -->
                <div class="bg-white rounded-xl shadow-lg overflow-hidden flex flex-col">
                    <div class="bg-brand-dark px-6 py-4">
                        <h3 class="text-2xl font-bold text-white">History of the Universe</h3>
                    </div>
                    <div class="p-6 flex-grow flex flex-col">
                        <p class="text-gray-700 mb-6 flex-grow">A full-blown journey from the first spark of the Big Bang to the emergence of Homo Sapiens on planet Earth.</p>
                        <a href="universe.html" class="block w-full text-center px-4 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-brand-teal hover:bg-teal-700 transition">
                            Explore Formats
                        </a>
                    </div>
                </div>

                <!-- Book 2 -->
                <div class="bg-white rounded-xl shadow-lg overflow-hidden flex flex-col">
                    <div class="bg-brand-dark px-6 py-4">
                        <h3 class="text-2xl font-bold text-white">Global Communication</h3>
                    </div>
                    <div class="p-6 flex-grow flex flex-col">
                        <p class="text-gray-700 mb-6 flex-grow">A collection of opinionated and potentially contentious thoughts designed to spark original conversations or wake up a few rusty old brains.</p>
                        <a href="comms.html" class="block w-full text-center px-4 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-brand-teal hover:bg-teal-700 transition">
                            Explore Formats
                        </a>
                    </div>
                </div>
            </div>
        </div>
    """
}

pages['universe.html'] = {
    'title': 'History of the Universe',
    'nav': 'nav_musings',
    'content': """
        <div class="max-w-5xl mx-auto">
            <div class="mb-8 flex items-center justify-between border-b pb-4">
                <h1 class="text-4xl font-bold text-gray-900">History of the Universe</h1>
                <a href="musings.html" class="text-brand-teal hover:underline">&larr; Back to Musings</a>
            </div>
            
            <div class="bg-white rounded-lg shadow-sm border border-gray-100 overflow-hidden mb-10">
                <div class="md:flex">
                    <div class="md:w-1/2 p-8 flex flex-col justify-center">
                        <p class="text-xl text-gray-700 leading-relaxed mb-6">
                            From the first spark of the Big Bang to the emergence of Homo Sapiens on planet Earth.
                        </p>
                        <p class="text-lg text-gray-700 leading-relaxed">
                            Upon completion, you will have a solid understanding of where and when we came from, and how the environment surrounding us formed and developed. You might be surprised by the depth and complexity of the trail leading away from those first few quarks, protons, electrons, and atoms... but I won't spoil the adventure.
                        </p>
                    </div>
                    <div class="md:w-1/2">
                        <img src="assets/img/andromadae.jpg" alt="Andromeda Galaxy" class="w-full h-full object-cover">
                    </div>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Door 1 -->
                <div class="bg-white rounded-lg shadow-lg overflow-hidden border-t-4 border-gray-800">
                    <div class="p-8">
                        <h2 class="text-2xl font-bold text-gray-900 mb-2">DOOR #1: Read the Book</h2>
                        <p class="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-6">83 Illustrated Pages (PDF)</p>
                        <p class="text-gray-700 mb-8">
                            The full illustrated manuscript. It traces our cosmic origins step-by-step, ensuring you have the best scientific information available to understand the transitions between each epoch.
                        </p>
                        <a href="assets/docs/create.pdf" class="flex justify-center items-center px-6 py-3 border-2 border-gray-800 text-base font-bold rounded-md text-gray-800 hover:bg-gray-800 hover:text-white transition">
                            Download Book PDF
                        </a>
                    </div>
                </div>

                <!-- Door 2 -->
                <div class="bg-white rounded-lg shadow-lg overflow-hidden border-t-4 border-brand-teal">
                    <div class="p-8">
                        <h2 class="text-2xl font-bold text-gray-900 mb-2">DOOR #2: Listen to the Podcast</h2>
                        <p class="text-sm font-semibold text-teal-600 uppercase tracking-wide mb-6">30 Minutes (AI Audio)</p>
                        <p class="text-gray-700 mb-8">
                            A relaxed alternative. AI has analyzed the entire manuscript and generated a highly realistic conversational podcast between two hosts. They discuss the book and highlight its key points.
                        </p>
                        
                        <div class="bg-gray-50 p-4 rounded-lg mb-6 border">
                            <p class="text-sm font-medium text-gray-700 mb-2">Play Podcast:</p>
                            <audio controls class="w-full">
                                <source src="assets/docs/create.mp3" type="audio/mpeg">
                                Your browser does not support the audio element.
                            </audio>
                        </div>

                        <a href="assets/docs/create.mp3" class="flex justify-center items-center px-6 py-3 border-2 border-brand-teal text-base font-bold rounded-md text-white bg-brand-teal hover:bg-teal-700 transition">
                            Download Audio MP3
                        </a>
                    </div>
                </div>
            </div>
        </div>
    """
}

pages['comms.html'] = {
    'title': 'Global Communication',
    'nav': 'nav_musings',
    'content': """
        <div class="max-w-5xl mx-auto">
            <div class="mb-8 flex items-center justify-between border-b pb-4">
                <h1 class="text-4xl font-bold text-gray-900">Global Communication</h1>
                <a href="musings.html" class="text-brand-teal hover:underline">&larr; Back to Musings</a>
            </div>
            
            <p class="text-xl text-gray-700 leading-relaxed mb-6">
                Being known as an opinionated individual, writing this book was an obvious direction for me to take. I had several ideas bursting at the seams to get out!
            </p>
            <p class="text-lg text-gray-700 leading-relaxed mb-10">
                The essays are designed to challenge common perceptions, hopefully forcing readers into some original conversations or at least sparking some brand new thoughts in a few rusty old brains.
            </p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <!-- Door 1 -->
                <div class="bg-white rounded-lg shadow-lg overflow-hidden border-t-4 border-gray-800">
                    <div class="p-8">
                        <h2 class="text-2xl font-bold text-gray-900 mb-2">DOOR #1: Read the Book</h2>
                        <p class="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-6">42 Pages (PDF)</p>
                        <p class="text-gray-700 mb-8">
                            The full Monty. 42 pages of potentially contentious opinions exploring how we communicate, connect, and think in a globalized era.
                        </p>
                        <a href="assets/docs/comms.pdf" class="flex justify-center items-center px-6 py-3 border-2 border-gray-800 text-base font-bold rounded-md text-gray-800 hover:bg-gray-800 hover:text-white transition">
                            Download Essay PDF
                        </a>
                    </div>
                </div>

                <!-- Door 2 -->
                <div class="bg-white rounded-lg shadow-lg overflow-hidden border-t-4 border-brand-teal">
                    <div class="p-8">
                        <h2 class="text-2xl font-bold text-gray-900 mb-2">DOOR #2: Listen to the Podcast</h2>
                        <p class="text-sm font-semibold text-teal-600 uppercase tracking-wide mb-6">15 Minutes (AI Audio)</p>
                        <p class="text-gray-700 mb-8">
                            A lively discussion. AI has reviewed the document and produced a remarkably realistic conversation between two hosts debating the main topics.
                        </p>
                        
                        <div class="bg-gray-50 p-4 rounded-lg mb-6 border">
                            <p class="text-sm font-medium text-gray-700 mb-2">Play Podcast:</p>
                            <audio controls class="w-full">
                                <source src="assets/docs/comms.mp3" type="audio/mpeg">
                                Your browser does not support the audio element.
                            </audio>
                        </div>

                        <a href="assets/docs/comms.mp3" class="flex justify-center items-center px-6 py-3 border-2 border-brand-teal text-base font-bold rounded-md text-white bg-brand-teal hover:bg-teal-700 transition">
                            Download Audio MP3
                        </a>
                    </div>
                </div>
            </div>
        </div>
    """
}

pages['personal.html'] = {
    'title': 'Personal Stories & Beliefs',
    'nav': 'nav_personal',
    'content': """
        <div class="max-w-5xl mx-auto">
            <h1 class="text-4xl font-bold text-gray-900 mb-8 border-b pb-4">Personal Stories & Philosophies</h1>
            
            <p class="text-xl text-gray-700 leading-relaxed mb-10">
                As if you haven't had enough of me already, here is a page dedicated to my personal experiences, stories, and opinions on a variety of topics. I make no assurances as to their acceptability or suitability, except to say that they are all G-rated!
            </p>

            <!-- Life Philosophies -->
            <div class="bg-brand-dark text-white rounded-xl shadow-lg p-8 mb-12">
                <h2 class="text-2xl font-bold mb-6 text-brand-teal">Thinking About Life</h2>
                <ul class="space-y-4 text-lg">
                    <li class="flex items-start"><span class="mr-3 mt-1 text-brand-teal">➔</span> <span>My primary job in life is to create as much <strong>serotonin and dopamine</strong> as I possibly can.</span></li>
                    <li class="flex items-start"><span class="mr-3 mt-1 text-brand-teal">➔</span> <span>I travel universally through the <strong>acquisition of information</strong>.</span></li>
                    <li class="flex items-start"><span class="mr-3 mt-1 text-brand-teal">➔</span> <span><strong>Understanding</strong> is my drug of choice.</span></li>
                    <li class="flex items-start"><span class="mr-3 mt-1 text-brand-teal">➔</span> <span>The <strong>past</strong> holds the secrets to who I am today.</span></li>
                    <li class="flex items-start"><span class="mr-3 mt-1 text-brand-teal">➔</span> <span>I am focus-driven on becoming the <strong>20-year-old</strong> that I always wanted to be.</span></li>
                </ul>
            </div>

            <h2 class="text-3xl font-bold text-gray-900 mb-8">Start of a Few Good Stories...</h2>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
                <!-- Adventures -->
                <div class="bg-white p-6 rounded-lg shadow border-t-4 border-red-500">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Adventures & Near Misses</h3>
                    <ul class="space-y-3 text-gray-700">
                        <li><strong>Plane Crash:</strong> Survived a single-engine plane crash.</li>
                        <li><strong>Skydiving:</strong> Completed a solo parachute jump (twice!).</li>
                        <li><strong>Mining:</strong> Mined 1/2 mile underground utilizing high explosives.</li>
                        <li><strong>Gunpoint:</strong> Had a gun pulled on me by an irate husband.</li>
                    </ul>
                </div>
                
                <!-- Media -->
                <div class="bg-white p-6 rounded-lg shadow border-t-4 border-blue-500">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Media & Public Life</h3>
                    <ul class="space-y-3 text-gray-700">
                        <li><strong>Game Show:</strong> Won the 1970s TV game show "Anything You Can Do".</li>
                        <li><strong>Headlines:</strong> Appeared on the front page of The Ottawa Citizen.</li>
                        <li><strong>Live TV:</strong> Solo guest speaker on a 1/2 hour live television broadcast.</li>
                        <li><strong>Theatre:</strong> Starred in a 3-act play featuring only two actors.</li>
                    </ul>
                </div>

                <!-- Professional -->
                <div class="bg-white p-6 rounded-lg shadow border-t-4 border-green-500">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Professional Highlights</h3>
                    <ul class="space-y-3 text-gray-700">
                        <li><strong>Teaching:</strong> Taught elementary school (grades 4-6) at age 19.</li>
                        <li><strong>Chess:</strong> Beat a Canadian Chess Grandmaster.</li>
                        <li><strong>Contracts:</strong> Wrote and managed three $50M public contracts.</li>
                        <li><strong>Retail:</strong> Managed "The Teacher's Store".</li>
                    </ul>
                </div>
            </div>

            <h2 class="text-3xl font-bold text-gray-900 mb-8">A Few Personal Beliefs</h2>
            <p class="text-gray-600 mb-6 italic">Click on each header below to expand my thoughts and opinions.</p>

            <div class="space-y-4 mb-12">
                <!-- Belief 1 -->
                <details class="group bg-white rounded-lg shadow border-l-4 border-purple-500">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-6 text-xl text-gray-900">
                        <span>Science</span>
                        <span class="transition group-open:rotate-180"><svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg></span>
                    </summary>
                    <div class="p-6 pt-0 text-gray-700 leading-relaxed border-t mt-4 pt-4">
                        <ul class="list-disc pl-6 space-y-2">
                            <li><strong>GMO Children:</strong> Children are really just the Genetically Modified Organisms of their parents.</li>
                            <li><strong>Stardust:</strong> Every single atom in your body came from within a distant, ancient star.</li>
                            <li><strong>The Living Cell:</strong> There is not a single living thing inside of any living cell.</li>
                            <li><strong>Evolution:</strong> Evolution is really just "Ha Ha, I'm Better Than You" played out over millions of years.</li>
                            <li><strong>Brain Sides:</strong> The left side of your brain sees the past; the right side of your brain sees the future.</li>
                            <li><strong>Sound:</strong> Sound is simply the brain’s internal expression of the world's acoustic vibrations.</li>
                        </ul>
                    </div>
                </details>

                <!-- Belief 2 -->
                <details class="group bg-white rounded-lg shadow border-l-4 border-yellow-500">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-6 text-xl text-gray-900">
                        <span>Religion & Destiny</span>
                        <span class="transition group-open:rotate-180"><svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg></span>
                    </summary>
                    <div class="p-6 pt-0 text-gray-700 leading-relaxed border-t mt-4 pt-4">
                        <ul class="list-disc pl-6 space-y-2">
                            <li><strong>Miraculous Complexity:</strong> Complexity is very often misinterpreted as "miraculous."</li>
                            <li><strong>Personal Divinity:</strong> Everyone is their own God.</li>
                            <li><strong>The Afterlife:</strong> Perspectives differ, but we can all agree there is no "life" remaining in this collective physical reality.</li>
                            <li><strong>The Collective Rule:</strong> If no one did IT, or if everyone did IT, would we all be better off?</li>
                            <li><strong>The Destination:</strong> We are all on the same train headed to the same destination, just traveling in different cars.</li>
                            <li><strong>Morality:</strong> Liars and cheaters are really just as bad as robbers and killers.</li>
                        </ul>
                    </div>
                </details>

                <!-- Belief 3 -->
                <details class="group bg-white rounded-lg shadow border-l-4 border-indigo-500">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-6 text-xl text-gray-900">
                        <span>People & Communication</span>
                        <span class="transition group-open:rotate-180"><svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg></span>
                    </summary>
                    <div class="p-6 pt-0 text-gray-700 leading-relaxed border-t mt-4 pt-4">
                        <ul class="list-disc pl-6 space-y-2">
                            <li><strong>The Workspace:</strong> Everyone feels overworked and underpaid.</li>
                            <li><strong>The Broadcast Problem:</strong> Many people are permanently stuck on "SEND" (rarely switching to receive).</li>
                            <li><strong>Privacy:</strong> There are some things that people just do not need to know about you.</li>
                            <li><strong>Mistakes vs. Wrong:</strong> Nobody is ever truly WRONG! They may, however, be temporarily mistaken.</li>
                        </ul>
                    </div>
                </details>

                <!-- Belief 4 -->
                <details class="group bg-white rounded-lg shadow border-l-4 border-pink-500">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-6 text-xl text-gray-900">
                        <span>Men & Women</span>
                        <span class="transition group-open:rotate-180"><svg fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg></span>
                    </summary>
                    <div class="p-6 pt-0 text-gray-700 leading-relaxed border-t mt-4 pt-4">
                        <ul class="list-disc pl-6 space-y-2">
                            <li><strong>Partnership:</strong> You first must BE "The One" before you can FIND "The One."</li>
                            <li><strong>Delegation:</strong> If you want a job done right, ask a woman. If you need an excuse for why a job can't be done, ask a man.</li>
                            <li><strong>Procreation:</strong> For males, it's much like taking a few cups of flour to a baker and returning in 9 months for the cake.</li>
                            <li><strong>Attraction:</strong> What many women really want is a good boy who can become a bad boy on command.</li>
                        </ul>
                    </div>
                </details>
            </div>

            <div class="text-center mt-12">
                <a href="population.html" class="inline-block text-brand-teal font-bold text-lg hover:underline">Also check out: Where Do You Fit In? (Population Calculator) &rarr;</a>
            </div>
        </div>
    """
}

pages['population.html'] = {
    'title': 'Population Calculator',
    'nav': 'nav_personal',
    'content': """
        <div class="max-w-4xl mx-auto">
            <div class="mb-8 flex items-center justify-between border-b pb-4">
                <h1 class="text-4xl font-bold text-gray-900">Where Do You Fit In?</h1>
                <a href="personal.html" class="text-brand-teal hover:underline">&larr; Back to Personal</a>
            </div>
            
            <div class="bg-white rounded-lg shadow p-8 mb-8">
                <p class="text-xl text-gray-700 leading-relaxed mb-8">
                    How does your age line up with the rest of the global population? This calculator was built to analyze demographic data and show you where you sit relative to the rest of the world.
                </p>
                
                <div class="bg-brand-peach-light border border-orange-200 rounded-lg p-6 flex flex-col md:flex-row items-center justify-between">
                    <div class="mb-4 md:mb-0">
                        <h3 class="text-2xl font-bold text-gray-900">Population Calculator Tool</h3>
                        <p class="text-gray-600 mt-1">Interactive Google Sheet analyzing population statistics.</p>
                        <p class="text-sm text-gray-500 mt-2">Format: Google Sheets</p>
                    </div>
                    <a href="https://docs.google.com/spreadsheets/d/1RB5z_NZ3b6hCRh_SVg9uxoyb8epqIcRuh8EJkZRecJg/edit?gid=0#gid=0" target="_blank" class="inline-flex items-center px-6 py-3 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-brand-teal hover:bg-teal-700 focus:outline-none transition">
                        <svg class="-ml-1 mr-3 h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                        </svg>
                        Open in Google Sheets
                    </a>
                </div>
            </div>
        </div>
    """
}

pages['tunes.html'] = {
    'title': 'Tunes',
    'nav': 'nav_tunes',
    'content': """
        <div class="max-w-5xl mx-auto">
            <h1 class="text-4xl font-bold text-gray-900 mb-8 border-b pb-4">Tunes: My Album</h1>
            
            <div class="bg-white rounded-lg shadow p-8 mb-12 border border-gray-100">
                <div class="md:flex items-center">
                    <div class="md:w-2/3 md:pr-8">
                        <p class="text-lg text-gray-700 leading-relaxed mb-4">
                            For many years, friends and family have heard me mention an "album." Well, for better or worse, this is it—mistakes and all. It is a little late now to correct the past, so there is no need to listen <em>too</em> carefully!
                        </p>
                        <p class="text-lg text-gray-700 leading-relaxed mb-4">
                            This is an eclectic collection spanning over 35 years of playing. It contains primarily original tunes and songs, recovered from very old recording room test tapes. Almost no one has ever heard me play guitar because I rarely played outside my own home.
                        </p>
                        <div class="bg-brand-peach-light border-l-4 border-orange-400 p-4 mt-6">
                            <p class="text-gray-800"><strong>Note on my journey:</strong> A slowly progressing Benign Tremor in both of my hands has finally curtailed my playing for good. But hey, "Better Late Than Never," right?</p>
                        </div>
                    </div>
                    <div class="md:w-1/3 mt-6 md:mt-0">
                        <img src="assets/img/guitar-756326_640.jpg" alt="Acoustic Guitar" class="rounded-lg shadow-md w-full border border-gray-200">
                    </div>
                </div>
            </div>

            <!-- Tracklist -->
            <h2 class="text-3xl font-bold text-gray-900 mb-8">The Track List</h2>

            <div class="space-y-8">
                <!-- Track 1 -->
                <div class="bg-white border rounded-xl shadow-sm overflow-hidden flex flex-col md:flex-row">
                    <div class="md:w-2/3 p-6">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">1. Look Into My Eyes <span class="text-sm font-normal text-gray-500">(3:38)</span></h3>
                        <p class="text-gray-700 mb-3"><strong>The Story:</strong> My first-ever love song. I was 21, working my first real job, and fell head-over-heels for my boss's wife at dinner. The result was this soul-searching look into the heart of a young boy.</p>
                        <p class="text-sm text-gray-600"><em>Technical:</em> Recorded circa 1971 on a brand new AKAI reel-to-reel tape deck. You can hear volume fluctuations during the first 10 seconds.</p>
                    </div>
                    <div class="md:w-1/3 bg-gray-50 p-6 border-l flex flex-col justify-center items-center">
                        <audio controls class="w-full mb-4">
                            <source src="assets/audio/Look_Into_My_Eyes.mp3" type="audio/mpeg">
                        </audio>
                        <a href="assets/audio/Look_Into_My_Eyes.mp3" class="text-sm text-brand-teal hover:underline" download>Download Audio</a>
                    </div>
                </div>

                <!-- Track 2 -->
                <div class="bg-white border rounded-xl shadow-sm overflow-hidden flex flex-col md:flex-row">
                    <div class="md:w-2/3 p-6">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">2. Dual in AM <span class="text-sm font-normal text-gray-500">(1:42)</span></h3>
                        <p class="text-gray-700 mb-3"><strong>The Story:</strong> An early overdubbing attempt. The deck allowed me to play a rhythm track and then replay it twice to overlay the "lead" guitar. It created an increasing echo with each track!</p>
                    </div>
                    <div class="md:w-1/3 bg-gray-50 p-6 border-l flex flex-col justify-center items-center">
                        <audio controls class="w-full mb-4">
                            <source src="assets/audio/Dual_in_AM.mp3" type="audio/mpeg">
                        </audio>
                        <a href="assets/audio/Dual_in_AM.mp3" class="text-sm text-brand-teal hover:underline" download>Download Audio</a>
                    </div>
                </div>

                <!-- Track 3 -->
                <div class="bg-white border rounded-xl shadow-sm overflow-hidden flex flex-col md:flex-row">
                    <div class="md:w-2/3 p-6">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">3. Dual in Em <span class="text-sm font-normal text-gray-500">(2:41)</span></h3>
                        <p class="text-gray-700 mb-3"><strong>The Story:</strong> A softer overdubbing output and my first experiment in <strong>Open E tuning</strong>. I learned this open-tuning technique after watching Joni Mitchell play open string a mere 10 feet in front of me at an Ottawa coffee house for $2.</p>
                    </div>
                    <div class="md:w-1/3 bg-gray-50 p-6 border-l flex flex-col justify-center items-center">
                        <audio controls class="w-full mb-4">
                            <source src="assets/audio/Dual_in_Em.mp3" type="audio/mpeg">
                        </audio>
                        <a href="assets/audio/Dual_in_Em.mp3" class="text-sm text-brand-teal hover:underline" download>Download Audio</a>
                    </div>
                </div>

                <!-- Track 4 -->
                <div class="bg-white border rounded-xl shadow-sm overflow-hidden flex flex-col md:flex-row">
                    <div class="md:w-2/3 p-6">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">4. One Day <span class="text-sm font-normal text-gray-500">(4:07)</span></h3>
                        <p class="text-gray-700 mb-3"><strong>The Story:</strong> My cover of Murray McLauchlan's "Revelations." It became my true personal anthem. I didn't realize I had been playing it slightly wrong for a while and missed recording the first chorus!</p>
                    </div>
                    <div class="md:w-1/3 bg-gray-50 p-6 border-l flex flex-col justify-center items-center">
                        <audio controls class="w-full mb-4">
                            <source src="assets/audio/One%20Day.m4a" type="audio/mpeg">
                        </audio>
                        <a href="assets/audio/One%20Day.m4a" class="text-sm text-brand-teal hover:underline" download>Download Audio</a>
                    </div>
                </div>
                
                <!-- Track 5 -->
                <div class="bg-white border rounded-xl shadow-sm overflow-hidden flex flex-col md:flex-row">
                    <div class="md:w-2/3 p-6">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">5. So Long</h3>
                        <p class="text-gray-700 mb-3"><strong>The Story:</strong> A personal favorite captured during those early recording sessions.</p>
                    </div>
                    <div class="md:w-1/3 bg-gray-50 p-6 border-l flex flex-col justify-center items-center">
                        <audio controls class="w-full mb-4">
                            <source src="assets/audio/So_Long.mp3" type="audio/mpeg">
                        </audio>
                        <a href="assets/audio/So_Long.mp3" class="text-sm text-brand-teal hover:underline" download>Download Audio</a>
                    </div>
                </div>

                <!-- Track 6 -->
                <div class="bg-white border rounded-xl shadow-sm overflow-hidden flex flex-col md:flex-row">
                    <div class="md:w-2/3 p-6">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">6. Halloween Rag</h3>
                        <p class="text-gray-700 mb-3"><strong>The Story:</strong> An upbeat, ragtime-style instrumental piece.</p>
                    </div>
                    <div class="md:w-1/3 bg-gray-50 p-6 border-l flex flex-col justify-center items-center">
                        <audio controls class="w-full mb-4">
                            <source src="assets/audio/Halloween_Rag.mp3" type="audio/mpeg">
                        </audio>
                        <a href="assets/audio/Halloween_Rag.mp3" class="text-sm text-brand-teal hover:underline" download>Download Audio</a>
                    </div>
                </div>

                <!-- Track 7 -->
                <div class="bg-white border rounded-xl shadow-sm overflow-hidden flex flex-col md:flex-row">
                    <div class="md:w-2/3 p-6">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">7. Norma</h3>
                        <p class="text-gray-700 mb-3"><strong>The Story:</strong> Dedicated to my wonderful partner, Norma.</p>
                    </div>
                    <div class="md:w-1/3 bg-gray-50 p-6 border-l flex flex-col justify-center items-center">
                        <audio controls class="w-full mb-4">
                            <source src="assets/audio/Norma.mp3" type="audio/mpeg">
                        </audio>
                        <a href="assets/audio/Norma.mp3" class="text-sm text-brand-teal hover:underline" download>Download Audio</a>
                    </div>
                </div>

                <!-- Track 8 -->
                <div class="bg-white border rounded-xl shadow-sm overflow-hidden flex flex-col md:flex-row">
                    <div class="md:w-2/3 p-6">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">8. Judy's Song</h3>
                        <p class="text-gray-700 mb-3"><strong>The Story:</strong> An original piece dedicated to family.</p>
                    </div>
                    <div class="md:w-1/3 bg-gray-50 p-6 border-l flex flex-col justify-center items-center">
                        <audio controls class="w-full mb-4">
                            <source src="assets/audio/Judys_Song.m4a" type="audio/mpeg">
                        </audio>
                        <a href="assets/audio/Judys_Song.m4a" class="text-sm text-brand-teal hover:underline" download>Download Audio</a>
                    </div>
                </div>

                <!-- Track 9 -->
                <div class="bg-white border rounded-xl shadow-sm overflow-hidden flex flex-col md:flex-row">
                    <div class="md:w-2/3 p-6">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">9. Amsterdam Night</h3>
                        <p class="text-gray-700 mb-3"><strong>The Story:</strong> Memories of European travels captured in an acoustic melody.</p>
                    </div>
                    <div class="md:w-1/3 bg-gray-50 p-6 border-l flex flex-col justify-center items-center">
                        <audio controls class="w-full mb-4">
                            <source src="assets/audio/Amsterdam_Night.mp3" type="audio/mpeg">
                        </audio>
                        <a href="assets/audio/Amsterdam_Night.mp3" class="text-sm text-brand-teal hover:underline" download>Download Audio</a>
                    </div>
                </div>

                <!-- Track 10 -->
                <div class="bg-white border rounded-xl shadow-sm overflow-hidden flex flex-col md:flex-row">
                    <div class="md:w-2/3 p-6">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">10. Aunts & Uncles</h3>
                        <p class="text-gray-700 mb-3"><strong>The Story:</strong> A tribute to the extended family branches and shared memories.</p>
                    </div>
                    <div class="md:w-1/3 bg-gray-50 p-6 border-l flex flex-col justify-center items-center">
                        <audio controls class="w-full mb-4">
                            <source src="assets/audio/Aunts_and_Uncles.mp3" type="audio/mpeg">
                        </audio>
                        <a href="assets/audio/Aunts_and_Uncles.mp3" class="text-sm text-brand-teal hover:underline" download>Download Audio</a>
                    </div>
                </div>

                <!-- Track 11 -->
                <div class="bg-white border rounded-xl shadow-sm overflow-hidden flex flex-col md:flex-row">
                    <div class="md:w-2/3 p-6">
                        <h3 class="text-2xl font-bold text-gray-900 mb-2">11. Take Me Along</h3>
                        <p class="text-gray-700 mb-3"><strong>The Story:</strong> Concluding the album journey with a classic acoustic track.</p>
                    </div>
                    <div class="md:w-1/3 bg-gray-50 p-6 border-l flex flex-col justify-center items-center">
                        <audio controls class="w-full mb-4">
                            <source src="assets/audio/TakeMeAlong.mp3" type="audio/mpeg">
                        </audio>
                        <a href="assets/audio/TakeMeAlong.mp3" class="text-sm text-brand-teal hover:underline" download>Download Audio</a>
                    </div>
                </div>
            </div>
        </div>
    """
}

pages['about.html'] = {
    'title': 'About',
    'nav': 'nav_about',
    'content': """
        <div class="max-w-4xl mx-auto">
            <h1 class="text-4xl font-bold text-gray-900 mb-8 border-b pb-4">About Us</h1>
            
            <!-- James and Norma section -->
            <div class="bg-white rounded-xl shadow-lg overflow-hidden mb-12">
                <div class="md:flex">
                    <div class="md:w-1/2 p-8 flex flex-col justify-center">
                        <h2 class="text-3xl font-bold text-gray-900 mb-4">James & Norma</h2>
                        <p class="text-lg text-gray-700 mb-4">
                            Welcome! We anchor the masthead and are glad you've stopped by to visit. Here is my partner Norma enjoying a glass of Guinness and myself with a Rickard's Red—our frequent choice for a brew when out and about.
                        </p>
                        <div class="bg-brand-light p-4 rounded-lg border border-teal-200 inline-block">
                            <p class="text-brand-teal font-bold">As of March 9, 2025, we celebrated our 44th anniversary together and are still going strong!</p>
                        </div>
                    </div>
                    <div class="md:w-1/2 bg-gray-200 flex items-center justify-center min-h-[300px] overflow-hidden">
                        <img src="assets/img/beers2.jpg" alt="James and Norma" class="max-w-full h-auto object-cover">
                    </div>
                </div>
            </div>

            <!-- The Three Names -->
            <h2 class="text-3xl font-bold text-gray-900 mb-6">Why "James * Jimmy * Jido"?</h2>
            <p class="text-lg text-gray-700 mb-8">You will see three names featured at the top of this website. Each represents a different era and facet of my life:</p>

            <div class="space-y-6">
                <!-- James -->
                <div class="bg-white p-6 rounded-lg shadow border-l-4 border-blue-600">
                    <h3 class="text-2xl font-bold text-gray-900 mb-2">JAMES: The Official Persona</h3>
                    <p class="text-gray-700 mb-2"><strong>The Origin:</strong> Rarely used in my personal life. I hadn't heard it used since my mother was angry with me around 1962, until I started traveling and needed it for my passport.</p>
                    <p class="text-gray-700"><strong>Represents:</strong> My official side—the financial guy, the tax representative, the bank person.</p>
                </div>

                <!-- Jimmy -->
                <div class="bg-white p-6 rounded-lg shadow border-l-4 border-green-500">
                    <h3 class="text-2xl font-bold text-gray-900 mb-2">JIMMY: The Creative Dreamer</h3>
                    <p class="text-gray-700 mb-2"><strong>The Origin:</strong> A childhood nickname revived by a work colleague as a term of endearment, which quickly spread among friends.</p>
                    <p class="text-gray-700"><strong>Represents:</strong> The social, creative, and musical side of me. The guy playing guitar and truly living the dream!</p>
                </div>

                <!-- Jido -->
                <div class="bg-white p-6 rounded-lg shadow border-l-4 border-brand-teal">
                    <h3 class="text-2xl font-bold text-gray-900 mb-2">JIDO: The Family Legacy</h3>
                    <p class="text-gray-700 mb-2"><strong>The Origin:</strong> An Arabic word for grandfather, which is how my step-grandchildren address me.</p>
                    <p class="text-gray-700"><strong>Represents:</strong> The grandfather looking out for their future, well-being, and preserving family history on this very website.</p>
                </div>
            </div>
        </div>
    """
}

# Generate files
output_dir = r"c:\Users\j-a-b\.gemini\antigravity\scratch\google_site"

# Create assets folders
os.makedirs(os.path.join(output_dir, 'assets', 'audio'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'assets', 'docs'), exist_ok=True)
os.makedirs(os.path.join(output_dir, 'assets', 'img'), exist_ok=True)

for filename, data in pages.items():
    # Set all nav classes to empty, then set the active one
    nav_kwargs = {
        'nav_home': '',
        'nav_why': '',
        'nav_who': '',
        'nav_musings': '',
        'nav_personal': '',
        'nav_tunes': '',
        'nav_about': ''
    }
    nav_kwargs[data['nav']] = 'active'
    
    html = LAYOUT.format(
        title=data['title'],
        content=data['content'],
        **nav_kwargs
    )
    
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
        
print("Successfully generated all HTML files.")
