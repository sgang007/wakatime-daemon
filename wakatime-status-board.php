<?php header("refresh: 900;"); ?>

<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">

<html>
<head>
	<style type="text/css">
			body, * {

			}

			body,div,dl,dt,dd,ul,ol,li,h1,h2,h3,h4,h5,h6,pre,form,fieldset,input,textarea,p,blockquote,th,td {
				margin: 0;
				padding: 0;
			}

			fieldset,img {
				border: 0;
			}

			/* Settin up the page */
			html, body, #main {
				overflow: hidden;
			}

			body {
				font-size: 24px;
				line-height: 28px;
			}

			tr {
				height: 32px;
			}

			td {
				font-size: 28px;
				line-height: 32px;
				text-align: center;
			}

			body, html, #main {
				background: transparent !important;
			}

			h2 {
				color: #7e7e7e;
				font-size: 30px;
				line-height: 18px;
				margin: 0px auto;
				padding-top: 20px;
				text-align: center;
				text-transform: uppercase;
			}
	</style>

	<title></title>
</head>

<body>
	<h2>Wakatime Projects</h2>

	<table>
		<tr>
			<th>Project</th>
			<th>Recorded Time</th>
		</tr>

		<?php
		function secondsToTime($seconds) {
			$dtF = new DateTime("@0");
			$dtT = new DateTime("@$seconds");

			return $dtF->diff($dtT)->format('%h:%i:%s');
		}

		$apikey = "<insert API key>";

		$contents = file_get_contents('https://wakatime.com/api/v1/users/current/stats/last_7_days?api_key='.$apikey);

		$wakatime_api = json_decode($contents);

		$projects = $wakatime_api->data->projects;

		if (count($projects)) {
	        // Cycle through the array
	        foreach ($projects as $idx => $project) {
	        	$time = secondsToTime($project->total_seconds);

	            // Output a row
	            echo "<tr>";
	            echo "<td>$project->name</td>";
	            echo "<td>$time</td>";
	            echo "</tr>";
	        }
	    }
		?>
	</table>
</body>
</html>
