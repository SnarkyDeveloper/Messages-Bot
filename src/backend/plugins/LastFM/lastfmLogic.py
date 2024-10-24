fm = "Reply with what's currently playing from your last.fm account."

def get_lastfm_now_playing(*args):
    if len(args) == 1:
        return "Enter a name to save"
    nameToSave = args[0]
    userObject = args[-1]

    try:
        userObject.name = nameToSave
    except AttributeError:
        userObject.addAttribute(attributeName="name", attributeValue=nameToSave)

    userObject.saveChanges()