from string import Template
INDEX_TEMPLATE = Template("""

<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
<link rel="stylesheet" href="https://code.getmdl.io/1.1.3/material.indigo-pink.min.css">
<script defer src="https://code.getmdl.io/1.1.3/material.min.js"></script>


<div class="mdl-grid">
  <div class="mdl-cell mdl-cell--4-col mdl-cell--4-offset">
}
<div id="player"></div>
<script src="http://www.youtube.com/player_api"> </script>
<script>
    
    // create youtube player
    var player;
    function onYouTubePlayerAPIReady() {
        player = new YT.Player('player', {
          height: '480',
          width: '835',
          videoId: '${yt_id}',
          events: {
            'onReady': onPlayerReady,
            'onStateChange': onPlayerStateChange
          }
        });
    }

    // autoplay video
    function onPlayerReady(event) {
        event.target.playVideo();
    }

    // when video ends
    function onPlayerStateChange(event) {        
        if(event.data === 0) {            
            location.reload(true);;
        }
    }
</script>

  </div>
</div>
  <footer class="mdl-mini-footer">
    <div class="mdl-mini-footer__left-section">
      <div class="mdl-logo"> (c) klauswunderlich.se 2016 </div>
      <ul class="mdl-mini-footer__link-list">
        <li><a href="https://github.com/skandix/klauswunderlich.se">github</a></li>
        <li><a href="https://twitter.com/sk4ndix">contact</a></li>
      </ul>
    </div>
  </footer>
""")