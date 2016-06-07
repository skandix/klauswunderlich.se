from string import Template
HTML_TEMPLATE = Template("""
      <h2>
        YouTube video link: 
        <a href="https://www.youtube.com/watch?v=${yt_id }">
          ${yt_id }
        </a>
      </h2>
    
      <iframe src="https://www.youtube.com/embed/${yt_id }" width="853" height="480" frameborder="0" allowfullscreen></iframe>""")
