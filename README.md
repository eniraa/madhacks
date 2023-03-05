## Inspiration
With two of our team members having extensive experience with competitive programming (e.g. USACO and ICPC), and all of us being "on the grind" for internships, we found ourselves wanting to be able to analyze our code's performance in an easy-to-use interface in order to gain insights on how we can improve the code. Moreover, we wanted to be able to generate time/space complexity analyses for our code, since no adequate tools exist.
## What it does
CodeScope runs user-submitted code with a given input (which is passed into stdin) and gives the output from stdout back to the user. Additionally, CodeScope also provides statistics on runtime, memory usage, code coverage (i.e. hot paths), and optionally, a time/space complexity analysis.
## How we built it
Our application uses Svelte and TypeScript for the frontend. This frontend is coupled with a backend using Flask. The backend runs several code analysis tools in short-lived Docker containers (which provides an easy way to extend the tool to work with many languages) to run the code and evaluate code performance. Because no existing tools provide good enough time/space complexity analysis, CodeScope uses OpenAI's models to generate such an analysis.
## Challenges we ran into
As anyone who does web development would know, CORS was a bit of a pain to deal with.

Apart from that, a lot of the challenge was in running our analysis tools so that they would be compatible with our architecture. For instance, when attempting to get memory statistics, we had originally intended on using something like `py-spy` or `psutil`. However, sometimes the code would finish too quickly for these tools to find the process it was running in, so they would be unable to provide memory statistics. We ended up writing and injecting our own code into a user's submission so that we could capture memory usage.
## Accomplishments that we're proud of
We are proud of developing a code analysis tool which meets the needs of competitive programmers and job seekers (e.g. us, other MadHacks hackers, etc.). We are also proud of learning the technologies needed to develop this application, as well as having ended up with a polished finished product.
## What we learned
Our backend developers learned about various code analysis/profiling tools, as well as how to run them in an isolated environment (i.e. Docker). Our frontend developers learned Svelte and Flowbite as well as how to make a web-based code editor.
## What's next for CodeScope
We could definitely support more languages, since our architecture allows for our backend to be easily extended to support new languages. Other than that, we could add more specific time/space statistics (i.e. runtime and memory usage per line of code). Lastly, we could also develop extensions for IDEs and browsers (so we could analyze user code in LeetCode or HackerRank editors).

## Running
The backend can be run by just running `python main.py`. The frontend can be run on a development environment through `npm run dev`. Install dependencies as needed through `poetry` and `npm`, and also make sure you have Docker installed.
