from headless.init import GithubHeadlessPage


page = GithubHeadlessPage()
# Login on github
page.login()
# Visit author's repo
page.move_around()
# Perform logout
page.logout()
