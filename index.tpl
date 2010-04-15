<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <title>IMDB API</title>
    </head>
    <body>
    	<h1>IMDB API</h1>
    	<h3>by Stavros Korokithakis</h3>
    	<p>
    		Well hello. I see you want to access IMDB. Well, this is your chance.
			This service is updated every day from the
			<a href="http://www.imdb.com/interfaces">IMDB data files</a> and you
			can access it with the ?name=<show name> URL parameter. For example,
			this is the episode list (in JSON) for
			<a href="/js/?name=how+i+met+your+mother">How I Met Your Mother</a>.
		</p>

        Instructions:
		<ol>
		<li>Use the "name" GET parameter followed by the urlencoded show name. If there
                are multiple shows with the same name, you can pass the "year" parameter as well
                to select a year. The script can now return JSONP, you can pass the "callback"
                parameter to get the data wrapped in a javascript function whose name is the
                value of the callback parameter (<a href="/js/?name=firefly&callback=imdbapi">example</a>).</li>
		<li>The URL /js/ returns data as text/html and /json/ returns data as application/json.
                Both use exactly the same parameters.</li>
		<li>You can use wildcards by using the percent sign, for example 
		<a href="/js/?name=how+i+met+%25+mother">"how i met % mother"</a> will work.</li>
		<li>If there are multiple show names, you will get a list of the 15 first
		that match your string (<a href="/js/?name=%25how%25">example</a>).</li>
		<li>If the show was not found, you will get "null".</li>
		</ol>
		
		<ul>
        <li>The source code for this service is
        <a href="http://github.com/skorokithakis/imdbapi">available on GitHub</a>.
        </li>
		<li>I have also written a script that will rename your show's video files using
		this and other services, you can find it here:
		<a href="http://github.com/skorokithakis/episode-renamer/">Episode renamer</a>.</li>
		<li>If you need to contact me, my email is 
		<a href="mailto:stavros@korokithakis.net">stavros@korokithakis.net</a>.</li>
		<li>My homepage is <a href="http://www.korokithakis.net">korokithakis.net</a>.</li>
		</ul>

		<p>
		Have fun!
		</p>
	</body>
</html>
