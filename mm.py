C1
ctr shift+p
create java project,no archtype
.com,demo
then create a the floder name demo and the repo name should be also same
click enter ,open msg
next create the folder name .gitthub and insude that another folder workflows
and the select gitthub and workflows and create a file maven.yml 
after this push this to github
go to github and last go to actions and check


C2

ctr shift+p
create java project,no archtype
.com,demo
then create a the floder name demo and the repo name should be also same
click enter ,open msg
next create the folder name .gitthub and insude that another folder workflows
and the select gitthub and workflows and create a file maven.yml 
and also create the jenkins file 
after this push this to github
next go to jenkins new item give any name and select pipeline
and the in congig partselect github project url
then select github hook trigger for GIT
defination -pipeline script from SCM
next add git repo link
main
script path-jenkinsfile
select-lightweight checkout
apply and save
build

go to settings in jenkins-there select plugins
there install -git plugin,maven integration plugin,pipeline plugin,slack notification
create another new item and select (free style)click ok
in congifaturation part there source code managment select-git put the reop link
chane to main
add build setup select-execute windows batch command ther in description type-echo jenkins
next in add post-build action select slack notification
after selecting the slack notification there aperes the many options select the box
apply and save

next go to settings in jenkins -select credintial-add cred=there select (secret text)
next go to slack API website there create new app-select from scratch-give app name as hub and in the place of select the workspace (name hello-odm9638)-give this name while creating the workspace

now we have to go to slack.com website therecreate new workspace-it will ask for sign in and then the workspace is created
now go to slack.com launch the workspace after launch is done there they provie a link down of that click on that
there in channels your workspace name should appear
now in slack API select your workspace from the dropdown given and then-create app
in the slack API only on the left side select-oAuth and permissions there u will see the -bot token scopes there u will also see the add an oAuth scope there select:(chat:write,chat:write.public,and commands)
then scroll up there u will see install to hello-odm9638 there select the verification token there -u can see bot user oauth token copy the code
and  click reinstall to hello-odm9638
  then after clicking that one pager appears click -allow
  after copying the bot user oauth token come back to jenkins in the place of secret paste the code an ID name-slack-token
  and save

  in jenkins go to settings there select system scroll to bottom  there in workspace your workspace name should appear and default channel -#all-hello-odm9638,click on the custom slack box and click test connection 
  there  it should apper sucess
  apply and save
  now go to app.slack there type (/invite@hub)-click on send

now run the jenkins which we hace created 2nd time
then in app.slack msg should apper


