## GitHub steps

![Steps](https://github.com/AKannad/BRIDGEUP_ClimateCoders/blob/master/guides/GitHub_dailySteps.png)

Tips:
* Use **git status** before you **push** to check if all your commits were recognized by **git**
* Check out our group cheat sheet for a quick refresher on **git** commands
* If you forget to **push** any changes from an earlier class, remember to do so before you **pull** any updates from my repository.
* Write descriptive commit messages ([tips](https://medium.com/@steveamaza/how-to-write-a-proper-git-commit-message-e028865e5791))


## Setting up Github!

*This is adapted from [Katy Abbott's guide](https://github.com/amnh/BridgeUP-STEM-Oceans-Six/blob/master/git-instructions.md)*

- [x] 1. Log into GitHub on your browser, and navigate to [https://github.com/AKannad/BRIDGEUP_ClimateCoders](https://github.com/AKannad/BRIDGEUP_ClimateCoders). This is the repository where we will store all of our code this year.

- [x] 2. Navigate to the right side of the window and click on &quot;Fork&quot;. This will save a new copy of the repository to your own GitHub account.

![fork a repo](https://github.com/amnh/BridgeUP-STEM-Oceans-Six/blob/master/photos/fork.png)

- [x] 3. Open up Terminal. Decide where you want to store your GitHub repository on your computer, and navigate there. 

Useful terminal commands:
   * **cd path/folder_name** navigates to a folder
   * **ls** shows all the files in your folder/directory.
   * **cd ..** moves you up one folder
   * **cd** (without any names after it) takes you to your home directory
Check out the terminal cheat sheet for a quick refresher on terminal commands: 
 
 - [x] 4. Once you're in the right location, clone your repository. This downloads a copy of your repository onto your computer. 
 In Terminal, type **git clone \<url\>**, where **\<url\>** is the URL of your forked repository.
    * To find this URL, go to your GitHub account, open the repositories tab, find the forked repository, and click on the green button on the right side that says, \"Clone or download.\" Copy the URL it gives you.
    
    ![clone url](https://github.com/AKannad/BRIDGEUP_ClimateCoders/blob/master/misc/GitHub_guide_1.png)
    
  Make sure you're cloning your _forked_ repository, not the original! You can tell because in the top left corner, where it says the name of the repository, it will also have a description that identifies where it was forked from. This is an example of me forking to a previous Helen Fellow's GitHub. 

  ![forked from](https://github.com/AKannad/BRIDGEUP_ClimateCoders/blob/master/misc/GitHub_guide_2.png)
  
  - [ ] 5. Now, we are going connect your local directory to GitHub so your computer knows where to save any changes you've made online. This is a quick diagram of what these different connections look like. Ignore the **git** commands for now.
  
  ![git connections](https://github.com/AKannad/BRIDGEUP_ClimateCoders/blob/master/guides/GitHub_dailySteps.png)
  
  - [ ] 6. Check that your origin is your forked repository by typing in **git remote -v** (**-v** or **-verbose** is simply asking **git** to list out the URL in addition to the names of the remote connections. 
  
  - [ ] 7. Now, let's connect to my repository so you can add in any new changes I've made to your local repository. 
    * Type **git remote add upstream** **https://github.com/AKannad/BRIDGEUP_ClimateCoders** in Terminal.
    * Now, type **git remote -v** again. You should see two remotes: One called **origin** that points to your own repository, and one called **upstream** that points to the original.
    * If you make a mistake, type in **git remote set_url upstream \<url\>** to reset the URL.

- [ ] 8. Add me as a collaborator to your repository — that way, I'll be able to see your work and integrate it into the main repository. Go to "Settings" in your repository, visit "Collaborators" and add my username (akannad) into the "Add collaborators" box. 

- [ ] 9. Let's edit and add our first file to the repository. I'm going to add a .txt file for you to fill out in the "about_me" folder on GitHub. First, you'll have to pull the changes from my updated repository onto your computer. 
    * In Terminal, type in **git pull upstream master**. **master** is the main branch of your repository. On GitHub, you can make new branches to edit files without worrying about messing up your original file. We'll learn how to do this at a later date when we start working on our research code. 

- [ ] 10. Navigate to the "about_me" folder on your computer and edit the "about_me.txt" file.

- [ ] 11. When you're ready, 
    * Type **git add about_me.txt**. This lets git know you're ready to make a change. If you make a lot of changes, you could also do **git add .** so all the changes are added.
    * Type **git commit -m** \"\<Your message here\>\". Change \[Your message here\] to explain why you&#39;re making the change – i.e. &quot;Adding in my name&quot; etc.
    * To make sure the changes have been made, type in **git status**.
    
- [ ] 12. Next, you&#39;ll upload this change to your online repository. Type **git push origin master**. This tells git to send the changes you made on the **master** branch of your repository to your forked repository on GitHub.

Congratulations! You just successfully pulled a file from an online repository, and pushed your changes back all using Terminal! You are a GitHub master in the making :sunglasses:
