import instaloader
import time
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings("ignore")

class GramGetter:
    def __init__(self, username, cookie_dict):
        self.L = instaloader.Instaloader()
        self.L.load_session_from_file(username, cookie_dict)
        self.username = username

    def get_user_info(self, username):
        try:
            profile = instaloader.Profile.from_username(self.L.context, username)
        except instaloader.exceptions.ProfileNotExistsException:
            return "Profile not found."

        privacy = "private" if profile.is_private else "public"
        link = f"https://www.instagram.com/{username}"
        pseudo = username
        name = profile.full_name
        date = ""
        profile_pic = profile.profile_pic_url
        cover_pic = ""
        nb_followees = profile.followees
        nb_followers = profile.followers
        nb_publications = profile.mediacount

        user_info = {
            "privacy": privacy,
            "link": link,
            "pseudo": pseudo,
            "name": name,
            "date": date,
            "profile_pic": profile_pic,
            "cover_pic": cover_pic,
            "nb_followees": nb_followees,
            "nb_followers": nb_followers,
            "nb_publications": nb_publications,
        }

        return user_info

    def get_followers_followings(self, username, nb_followers, nb_following):
        try:
            profile = instaloader.Profile.from_username(self.L.context, username)
        except instaloader.exceptions.ProfileNotExistsException:
            return "Profile not found."

        followers = []
        followings = []

        for idx, follower in enumerate(profile.get_followers()):
            if idx >= nb_followers:
                break
            followers.append({
                'name': follower.full_name,
                'user_id': follower.username,
                'link': f'https://www.instagram.com/{follower.username}',
                'profile_pic': follower.profile_pic_url
            })
            time.sleep(5)

        for idx, following in enumerate(profile.get_followees()):
            if idx >= nb_following:
                break
            followings.append({
                'name': following.full_name,
                'user_id': following.username,
                'link': f'https://www.instagram.com/{following.username}',
                'profile_pic': following.profile_pic_url
            })
            time.sleep(5)

        return (followers, followings)


    def get_publications_from_search(self,user_id, nb_comments=20, since=None, nb_publications=20):
        try:
            profile = instaloader.Profile.from_username(self.L.context, user_id)
        except instaloader.exceptions.ProfileNotExistsException:
            return "Profile not found."
        publications = []
        comments = []
        idxxd=0
        if since:
            since = datetime.strptime(since, "%Y-%m-%d %H:%M:%S")
            for  post in profile.get_posts():
                date_of_post=post.date_utc.strftime('%Y-%m-%d %H:%M:%S')
                date_of_post=datetime.strptime(date_of_post, "%Y-%m-%d %H:%M:%S")
                if date_of_post >= since:
                    # Increment idx only if the date_of_post is greater or equal to since
                    idxxd += 1
                    if post.typename == "GraphSidecar":
                        images = [media.display_url for media in post.get_sidecar_nodes() if not media.is_video]
                        videos = [media.video_url for media in post.get_sidecar_nodes() if media.is_video]
                    elif post.typename == "GraphImage":
                        images = [post.url]
                        videos = []
                    else:
                        images = []
                        videos = [post.video_url]

                    # Get the post URL
                    post_url = f'https://www.instagram.com/p/{post.shortcode}/'
                    publication = {
                        'author': post.owner_username,
                        'contenu': post.caption,
                        'likes': post.likes,
                        'date': post.date_utc.strftime('%Y-%m-%d %H:%M:%S'),
                        'url': post_url,
                        'image': images,
                        'video': videos,
                        'number_of_comments': post.comments
                    }
                    publications.append(publication)

                    # Get the comments
                    post_comments = []
                    if post.comments > 0:
                        for idx, comment in enumerate(post.get_comments()):
                            if idx >= nb_comments:
                                break

                            replies_count = sum(1 for _ in comment.answers)

                            post_comments.append({
                                'user': comment.owner.username,
                                'profile_pic': comment.owner.profile_pic_url,
                                'comment': comment.text,
                                'date': comment.created_at_utc.strftime('%Y-%m-%d %H:%M:%S'),
                                'number_of_replies': replies_count,
                                'likes': comment.likes_count,
                                'publication_url': post_url,
                                'image': [],  # List of links of images is not provided by Instaloader
                                'emoji': [],  # List of links of emojis is not provided by Instaloader
                                'comment_url': ''  # Comment URL is not provided by Instaloader
                            })
                            time.sleep(2)  # Sleep for 2 seconds between fetching comments
                    comments.append(post_comments)

                    time.sleep(10)  # Sleep for 10 seconds between fetching posts
                    if idxxd >= nb_publications:
                        break
                else :
                    pass
        else :
            for idx, post in enumerate(profile.get_posts()):
                date_of_post=post.date_utc.strftime('%Y-%m-%d %H:%M:%S')
                date_of_post=datetime.strptime(date_of_post, "%Y-%m-%d %H:%M:%S")
                if idx >= nb_publications:
                    break

                if  date_of_post < since:
                    pass
                
                # Get the post information
                # Get the post information
                if post.typename == "GraphSidecar":
                    images = [media.display_url for media in post.get_sidecar_nodes() if not media.is_video]
                    videos = [media.video_url for media in post.get_sidecar_nodes() if media.is_video]
                elif post.typename == "GraphImage":
                    images = [post.url]
                    videos = []
                else:
                    images = []
                    videos = [post.video_url]

                # Get the post URL
                post_url = f'https://www.instagram.com/p/{post.shortcode}/'
                publication = {
                    'author': post.owner_username,
                    'contenu': post.caption,
                    'likes': post.likes,
                    'date': post.date_utc.strftime('%Y-%m-%d %H:%M:%S'),
                    'url': post_url,
                    'image': images,
                    'video': videos,
                    'number_of_comments': post.comments
                }
                publications.append(publication)

                # Get the comments
                post_comments = []
                if post.comments > 0:
                    for idx, comment in enumerate(post.get_comments()):
                        if idx >= nb_comments:
                            break

                        replies_count = sum(1 for _ in comment.answers)

                        post_comments.append({
                            'user': comment.owner.username,
                            'profile_pic': comment.owner.profile_pic_url,
                            'comment': comment.text,
                            'date': comment.created_at_utc.strftime('%Y-%m-%d %H:%M:%S'),
                            'number_of_replies': replies_count,
                            'likes': comment.likes_count,
                            'publication_url': post_url,
                            'image': [],  # List of links of images is not provided by Instaloader
                            'emoji': [],  # List of links of emojis is not provided by Instaloader
                            'comment_url': ''  # Comment URL is not provided by Instaloader
                        })
                        time.sleep(2)  # Sleep for 2 seconds between fetching comments
                comments.append(post_comments)

                time.sleep(10)  # Sleep for 10 seconds between fetching posts

        return publications, comments

    def pseudo_exists(self, user_id):
        try:
            instaloader.Profile.from_username(self.L.context, user_id)
            return True
        except instaloader.exceptions.ProfileNotExistsException:
            return False

    def publication_exists(self, pub_link):
        try:
            post = instaloader.Post.from_shortcode(self.L.context, pub_link.rsplit('/', 2)[-2])
            return True
        except:
            return False

    def private_account(self, username):
        try:
            profile = instaloader.Profile.from_username(self.L.context, username)
        except instaloader.exceptions.ProfileNotExistsException:
            return "Profile not found."

        privacy = True if profile.is_private else False
        return privacy

    def get_publication_from_pub_page(self, link, pseudo_user):
        if self.publication_exists(link):
            shortcode = link.rsplit('/', 2)[-2]
            post = instaloader.Post.from_shortcode(self.L.context, shortcode)

            if post.owner_username != pseudo_user:
                return "The provided pseudo_user does not match the publication owner."

            if post.typename == "GraphSidecar":
                images = [media.display_url for media in post.get_sidecar_nodes() if not media.is_video]
                videos = [media.video_url for media in post.get_sidecar_nodes() if media.is_video]
            elif post.typename == "GraphImage":
                images = [post.url]
                videos = []
            else:
                images = []
                videos = [post.video_url]

            publication = {
                'author': post.owner_username,
                'contenu': post.caption,
                'likes': post.likes,
                'date': post.date_utc.strftime('%Y-%m-%d %H:%M:%S'),
                'url': link,
                'image': images,
                'number_of_comments': post.comments,
            }

            return [publication]
        else:
            return "Publication does not exist"
    
    def get_stories(self,user_id: str):
        try:
            user = instaloader.Profile.from_username(self.L.context, user_id)
            stories = self.L.get_stories(userids=[user.userid])

            story_list = []

            for story in stories:
                for item in story.get_items():
                    is_video = item.is_video
                    story_dict = {
                        'author': user.username,
                        'contenu': "",
                        'likes': "",
                        'date': item.date_utc.strftime('%Y-%m-%d %H:%M:%S'),
                        'url': "",
                        'image': [item.url] if not is_video else [],
                        'video': [item.video_url] if is_video else [],
                        'number_of_comments': "",
                    }

                    story_list.append(story_dict)

            return (story_list, [])

        except Exception as e:
            print(f"Error: {e}")
            return ([], [])

    def get_comments_from_post(self, since=None, direct=False, direct_link=None, nb_comments=20):
        if direct:
            if self.publication_exists(direct_link):
                shortcode = direct_link.rsplit('/', 2)[-2]
                post = instaloader.Post.from_shortcode(self.L.context, shortcode)
            else:
                return "Publication does not exist"
        else:
            return "Direct mode is False. Please provide a direct link."

        post_comments = []

        if since:
            since = datetime.strptime(since, "%Y-%m-%d %H:%M:%S")

        if post.comments > 0:
            for idx, comment in enumerate(post.get_comments()):
                if idx >= nb_comments:
                    break

                comment_date = comment.created_at_utc.strftime('%Y-%m-%d %H:%M:%S')
                comment_date = datetime.strptime(comment_date, "%Y-%m-%d %H:%M:%S")
                
                if since and comment_date < since:
                    continue

                replies_count = sum(1 for _ in comment.answers)

                post_comments.append({
                    'user': comment.owner.username,
                    'profile_pic': comment.owner.profile_pic_url,
                    'comment': comment.text,
                    'date': comment.created_at_utc.strftime('%Y-%m-%d %H:%M:%S'),
                    'number_of_replies': replies_count,
                    'likes': comment.likes_count,
                    'publication_url': f'https://www.instagram.com/p/{post.shortcode}/',
                    'image': [],  # List of links of images is not provided by Instaloader
                    'emoji': [],  # List of links of emojis is not provided by Instaloader
                    'comment_url': ''  # Comment URL is not provided by Instaloader
                })
                time.sleep(2)  # Sleep for 2 seconds between fetching comments

        return post_comments
