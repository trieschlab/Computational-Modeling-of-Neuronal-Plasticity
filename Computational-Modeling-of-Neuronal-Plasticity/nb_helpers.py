from IPython.display import Image, IFrame
from myst_nb import glue

class OurYTVideo(IFrame):
    # like IPython.display.YouTubeVideo
    # - without JPEG representation
    # - with empty text representation
    def __init__(self, id, width=800, height=450, allow_autoplay=False, **kwargs):
        self.id=id
        src = "https://www.youtube.com/embed/{0}".format(id)
        if allow_autoplay:
            extras = list(kwargs.get("extras", [])) + ['allow="autoplay"']
            kwargs.update(autoplay=1, extras=extras)
        super(OurYTVideo, self).__init__(src, width, height, **kwargs)
    
    
    def __repr__(self):
        return ""


def glue_yt(label, ytid):
    vid = OurYTVideo(ytid)
    # if we display it directly there's a black box around the empty text returned by __repr__
    glue(label, vid, display=False)
