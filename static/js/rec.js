//webkitURL is deprecated but nevertheless


var gumStream; 						//stream from getUserMedia()
var rec; 							//Recorder.js object
var input; 							//MediaStreamAudioSourceNode we'll be recording

// shim for AudioContext when it's not avb. 
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext //audio context to help us record

var recordButton = document.getElementById("recordButton");
var stopButton = document.getElementById("stopButton");


//document.getElementById("stopButton").style.display = "none";
//document.getElementById("recordButton").style.display = "block";
document.getElementById("recordButton").classList.add('notRec');
document.getElementById("stopButton").classList.add('invisible');

//add events to those 2 buttons


recordButton.addEventListener("click", startRecording);
stopButton.addEventListener("click", stopRecording);

function startRecording() {
	console.log("recordButton clicked");
	//document.getElementById("recordButton").style.display = "none";

	document.getElementById("stopButton").classList.remove('invisible');

	
	document.getElementById("recordButton").classList.add('invisible');
	//document.getElementById("stopButton").style.display = "block";
	//document.getElementById("stopButton").style.alignContent = "center";
	// document.getElementById("stopButton").style.align="center";
	document.getElementById("stopButton").classList.add('Rec');
	//document.getElementById("b1").classList.add('btnable');
	//document.getElementById("b2").classList.add('btnable');
	
	/*
		Simple constraints object, for more advanced audio features see
		https://addpipe.com/blog/audio-constraints-getusermedia/
	*/
    
  var constraints = {
    audio: {
        sampleRate: 48000,
        sampleSize: 32,
    },
    video: false
};

 	/*
    	Disable the record button until we get a success or fail from getUserMedia() 
	*/

	recordButton.disabled = true;
	stopButton.disabled = false;

	/*
    	We're using the standard promise based getUserMedia() 
    	https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
	*/

	navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
		console.log("getUserMedia() success, stream created, initializing Recorder.js ...");

		/*
			create an audio context after getUserMedia is called
			sampleRate might change after getUserMedia is called, like it does on macOS when recording through AirPods
			the sampleRate defaults to the one set in your OS for your playback device

		*/
		audioContext = new AudioContext({
			latencyHint: 'interactive',
  			sampleRate: 48000,
  			sampleSize: 32,
		});

		//update the format 
		//document.getElementById("formats").innerHTML="Format: 1 channel pcm @ "+audioContext.sampleRate/1000+"kHz"

		/*  assign to gumStream for later use  */
		gumStream = stream;
		
		/* use the stream */
		input = audioContext.createMediaStreamSource(stream);

		/* 
			Create the Recorder object and configure to record mono sound (1 channel)
			Recording 2 channels  will double the file size
		*/
		rec = new Recorder(input,{numChannels:2})

		//start the recording process
		rec.record()
		console.log(audioContext.sampleRate);
		console.log("Recording started");

	}).catch(function(err) {
	  	//enable the record button if getUserMedia() fails
    	recordButton.disabled = false;
    	stopButton.disabled = true;
	});
}


function stopRecording() {
	//document.getElementById("stopButton").style.display = "none"


	document.getElementById("stopButton").classList.add('invisible');
	document.getElementById("recordButton").classList.remove('invisible');
	//document.getElementById("recordButton").style.display = "block";
	document.getElementById("recordButton").classList.add('notRec');
	console.log("stopButton clicked");

	//disable the stop button, enable the record too allow for new recordings
	stopButton.disabled = true;
	recordButton.disabled = true;

	//reset button just in case the recording is stopped while paused
	
	//tell the recorder to stop the recording
	rec.stop();

	//stop microphone access
	gumStream.getAudioTracks()[0].stop();

	//create the wav blob and pass it on to createDownloadLink
	rec.exportWAV(createDownloadLink);
}

function createDownloadLink(blob) {
	
	//var url = URL.createObjectURL(blob);
	//var au = document.createElement('audio');
	//var li = document.createElement('li');
	//var link = document.createElement('a');

	//name of .wav file to use during upload and download (without extendion)
	var filename = new Date().toISOString();
	
	//upload link

	var upload = document.createElement('a');
	upload.href = new_page;
	console.log(new_page);
	upload.innerHTML = "upload";
	upload.addEventListener("click", function(event){
		  var xhr=new XMLHttpRequest();
		  xhr.onload=function(e) {
		      if(this.readyState === 4) {
		          console.log("Server returned: ",e.target.responseText);

	      }
};
		  var fd=new FormData();
		  fd.append("audio_data",blob, filename);
		  xhr.open("POST","/recorder/" + ques_no +"/",true);
		  console.log("/recorder/"+ ques_no +"/")
	function getCookie(name) {
    	var cookieValue = null;
    	if (document.cookie && document.cookie !== '') {
        	var cookies = document.cookie.split(';');
        	for (var i = 0; i < cookies.length; i++) {
            	var cookie = jQuery.trim(cookies[i]);
            	// Does this cookie string begin with the name we want?
            	if (cookie.substring(0, name.length + 1) === (name + '=')) {
                	cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                	break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
		  xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
		  xhr.send(fd);
	})
	//li.appendChild(document.createTextNode (" "))//add a space in between
	//li.appendChild(upload)//add the upload link to li

	//add the li element to the ol
	recordingsList.appendChild(upload);
}
