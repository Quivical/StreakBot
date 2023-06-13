<h1>Acitivty Logger Discord Bot</h1>

<h2>Overview</h2>
<p>A bot designed to encourage doing a daily activity, such as studying or even washing the dishes.
The bot allows server members to log that they have completed the activity daily using /log. A user's historical activity can be viewed on their profile using /profile or compared to other users on the leaderboard using /leaderboard.
</p>

<h2>Deployment</h2>
<p>There is no hosted solution for this bot and you must host it yourself. Note that the bot is only designed for to work in one guild/server. While multiple is possible, data will be shared amongst each. To deploy the bot, please see the instructions below:</p>
 <ol>
  <li>Ensure you are running Python 3.11 (untested in other Python versions, but may still work).</li>
  <li>Set up a virtual environment using venv and install the dependencies.<br>To setup venv: <code>py -m venv venv</code> (See <a href="https://docs.python.org/3/library/venv.html">docs</a> for more)<br>Install dependencies: <code>pip install -U -r requirements.txt</code></li>
  <li>Rename <code>config.py.example</code> to <code>config.py</code> and modify where applicable.</li>
  <li>Rename <code>.env.example</code> to <code>.env</code> and modify where applicable.<br>Get token from the <a href="https://discord.com/developers/applications">Discord Developer Portal</a></li>
  <li>Run the bot using <code>py main.py</code>.</li>
</ol>

<p>Support for the bot is avaliable, but not guaranteed, via Discord (username: samln) or by creating a GitHub issue. </p>
