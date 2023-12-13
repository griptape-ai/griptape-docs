__What is Griptape Cloud?__

Griptape Cloud is a managed web service that you can use to deploy and run AI-enabled python applications. You can write conversational agents, sequential pipelines, or complex workflows using the griptape framework, and then simply upload them to Griptape Cloud when you are ready to test and publish them; we’ll take care of provisioning and managing the underlying infrastructure.

Griptape Cloud is currently in a private preview evaluation phase intended for development and testing purposes.

__How do I access Griptape Cloud?__

1. Check your email for a message from hello@griptape.ai containing your temporary Griptape Cloud login credentials. 
2. Go to https://cloud-preview.griptape.ai.
3. Sign in with the credentials provided in your invitation email, or Sign in with Google using the same email at which you received the invitation. 

__How do I deploy my first Griptape Cloud app?__

You can deploy a Griptape Cloud app using the Griptape CLI or the web browser interface. To deploy an app from the web interface:
1. Sign in at https://cloud-preview.griptape.ai.
2. Click "New App" in the left navigation menu.
3. Upload a .zip archive file containing your application files. To upload the .zip file, drag and drop it onto the button labeled “Got an App?”, or click the button to browse for your file.
4. Your app is now deploying. When deployment succeeds, the blinking blue light next to the name of your app will turn to solid green. You can also check deployment status by clicking the Deployments tab.
5. You can now run your app. Try typing a prompt into the chat window.


!!! info

    "Your .zip archive file should contain the following files."

    - An app file named app.py to run the main application. Be sure to define the method in app.py to return a Griptape structure as follows:  def init_structure(*args) -> Structure:
    - A .env file that defines any necessary environment variables, such as API keys/values.
    - A requirements.txt file that defines any other requirements, such as which version of the griptape framework your app should use.
        
    Make sure each of these is at the top level of the archive file structure (not inside a folder).

    
__What can I expect during this preview phase?__

Over the coming weeks, you can expect a lot of new features, some bugs, and maybe a few breaking changes. We may also reach out to you for feedback about your experience, or to ask you to try out certain features.

__What do you expect from me, as a preview user?__

We want your feedback! Our goal for this private preview phase is to learn as much as we can about customers’ use cases, needs, and pain points to inform our continued development of Griptape Cloud.

__How do I provide feedback or request technical assistance?__

When you are signed in to Griptape Cloud in a browser, click the circular pink Intercom button at the lower right corner of the screen, and then send us a message. We look forward to your feedback, bug reports, and feature suggestions. We’d also be happy to help you troubleshoot problems. 



