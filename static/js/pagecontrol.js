function redirect(vidID)
			{
				setTimeout(function() {
				  window.location.href = "http://youtube.com/watch?v=" + vidID;
				}, 1000);
			}