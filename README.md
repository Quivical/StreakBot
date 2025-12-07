<h1>Acitivty Logger Discord Bot</h1>

<p><i>This project is a fork of <a href="https://github.com/SamNuttall/Activity-Log-Bot">Activity-Log-Bot</a>.</i></p>

<h2>Overview</h2>
<p>A bot designed to encourage doing a daily activity, such as studying or even washing the dishes.
The bot allows server members to log that they have completed the activity daily and then view their profile + sticker collection and see their activity in relation to other users on the leaderboard.
</p>

<h2>Commands</h2>
<ul>
  <li><b>/log</b> - Log that you have completed a daily activity.</li>
    <li><b>/profile</b> - View your or another user's profile which shows how many days they have logged, their streak, and sticker collection.</li>
    <li><b>/leaderboard</b> - See the leaderboard which shows which users have the highest streak and most days logged.</li>
<li><b>/sticker add</b> - Add a sticker to the library, which can be collected by using /log (moderator/admin only).</li>
<li><b>/remindme</b> - Optionally configure a time (in UTC) when the bot should remind you to log if you haven't done so already.</li>
</ul>

<h2>Deployment</h2>
<p>There is no hosted solution for this bot and you must host it yourself. Note that the bot is only designed for to work in one guild/server. While multiple is possible, data will be shared amongst each. To deploy the bot, please see the instructions below according to the type of deployment you'd like to run:</p>
<h5>Standalone Deployment (e.g. in a terminal, on a vm, etc.)</h5>
<ol>
  <li>Ensure you are running Python 3.11 (untested in other Python versions, but may still work).</li>
  <li>Set up a virtual environment using venv and install the dependencies.<br>To setup venv: <code>py -m venv venv</code> (See <a href="https://docs.python.org/3/library/venv.html">docs</a> for more)<br>Install dependencies: <code>pip install -U -r requirements.txt</code></li>
  <li>Rename <code>config.py.example</code> to <code>config.py</code> and modify where applicable.</li>
  <li>Rename <code>.env.example</code> to <code>.env</code> and modify where applicable.<br>Get token from the <a href="https://discord.com/developers/applications">Discord Developer Portal</a></li>
  <li>Run the bot using <code>py main.py</code>.</li>
</ol>
<h5>In A Docker Container</h5>
<ol>
  <li>Download and install docker desktop on your development envirement.</li>
  <li>From within the working directory, run <code>docker build -t [your_chosen_title_here] .</code> - note the period at the end of that command.</li>
  <li>Give the generated image a tag with <code>docker tag</code>.</li>
  <li>Push the code to a docker registry with <code>docker push</code>.</li>
  <li>With the docker daemon installed on your server, use <code>docker pull</code> to get the image.</li>
  <li>Finally, use <code>docker run</code> to start the bot. You may consider mounting a volume such that user data persists if you restart the bot, using flags like <code>-v ./db.sqlite:/app/db.sqlite</code>></li>
  <li><b>WARNING: This Docker build process hardcodes your bot's API key directly into the image. This is a significant security risk, as a publicly accessible image could expose your API key to unauthorized users. It is highly recommended to use a private Docker image for deployment. Additionally, always ensure your bot's API key is configured with the absolute minimum required permissions to mitigate potential abuse.</b></li>
</ol>

<p>Support for the bot is avaliable, but not guaranteed, via Discord (username: quivical) or by creating a GitHub issue. </p>
