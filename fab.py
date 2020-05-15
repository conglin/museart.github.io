import os
from fabric import task
from invoke import Exit

DEPLOY_PATH = "/Users/user/projects/blog"
deploy_path = "/Users/user/projects/blog"
theme_path = "/Users/user/Documents/projects/twenty-pelican-html5up"

@task
def collectstatic(c):
  if os.path.isdir(DEPLOY_PATH):
    c.local('mkdir -p {deploy_path}/css/ {deploy_path}/js/ {deploy_path}/fonts/ {deploy_path}/images/'.format(**c.env))
    c.local('cp -rf {theme_path}/static/css/* {deploy_path}/css/'.format(**c.env))
    c.local('cp -rf {theme_path}/static/js/* {deploy_path}/js/'.format(**c.env))
    c.local('cp -rf {theme_path}/static/fonts/* {deploy_path}/fonts/'.format(**c.env))
    c.local('cp -rf {theme_path}/static/images/* {deploy_path}/images/'.format(**c.env))