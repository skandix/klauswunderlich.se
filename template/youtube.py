from string import Template
HTML_TEMPLATE = Template("""<center><p>
        YouTube video link: 
        <a href="https://www.youtube.com/watch?v=${yt_id}?autoplay=1">
        </a>
      </p>
    
      <iframe src="https://www.youtube.com/embed/${yt_id}?autoplay=1" width="853" height="480" frameborder="0" allowfullscreen></iframe></center>
    """)
