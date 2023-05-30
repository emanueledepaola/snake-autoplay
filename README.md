# Quickstart Guide

Follow these simple steps to fire up a Linux host &ndash; with full control over it &ndash; and anything you need, just in a couple commands!

### TL;DR

- [GitHub Codespace setup](#github-codespace-setup)
- [Docker setup](#docker-setup)

If interested in understanding what's happening under the hood: in a few words, a containerized dev environment is instantiated in both cases (here below &ndash; locally, with Docker or in the cloud, with GitHub). There, every tool we need to develop (an IDE and the CLI) is accessible from the browser itself. 

What we miss is just a GUI to render `pygame` graphics.

To overcome this issue, thanks to the `pygbag` module, fortunately we can access the game as a webapp on a browser-based GUI. More info on this package at the following links:
- [Python Package](https://pypi.org/project/pygbag/)
- [Project Page](https://pygame-web.github.io/)
- [GitHub Repo](https://github.com/pygame-web/pygbag)

## GitHub Codespace setup

This is the quickest way to spin up a lightweight dev environment (in the cloud), without having to install anything on your personal computer, althougth sacrifying to some extent full access to resources and the overall control, over this environment.

Once logged-in on [GitHub](https://github.com/), navigate to the repo [andreagalle/snake-autoplay](https://github.com/andreagalle/snake-autoplay) and click on the `Use this template > Open in a codespace` button 

![Open Codespace](/img/open_codespace.png)

This will open a browser-based IDE (essentially vscode) in a new tab. As you instantiate this particular codespace, from the integrated CLI launch the setup script, after having sourced the hidden `.env` file:

    source .env
    setup

to install (first time only) all the dependecies we need, basically `pygame` and a custom version of `pygbag` modules.

Then, launch the deploy script:

    deploy

this basically use `pygbag` module passing the GitHub `${CODESPACE_NAME}` environment variable, to deploy the game on that domain name (randomly choosed by GitHub itself), under the default port `8000`.

![Open Codespace](/img/url_codespace.png)

This domain name must coincide with the string highlighted in the above URL thus, launching the deploy script would be the same as running the following command, for instance:

    pygbag --gh_codespace "andreagalle-animated-space-zebra" main.py

passing the `"andreagalle-animated-space-zebra"` codespace name itself, randomly assigned by GitHub itself. That's important to remember, just in case the `${CODESPACE_NAME}` environment variable won't work anymore in the future!

![Open Codespace](/img/animated_space_zebra.png)
( *"An animated space zebra in the style of vector artwork."* prompted to [DALL·E 2 - OpenAI](https://labs.openai.com/ ) on the 16th March 2023.)

Now click on the `Ready to start!` button, navigate the menu to choose the game mode and that's it!

**N.B.** always remember to turn off the codespace we just instantiated, not to waste useful resources (i.e. core hours used). Thus click on the GitHub `Codespace` tab at the Top Navigation Bar of the repo

![Open Codespace](/img/bar_codespace.png)

then, search for the (randomly generated) name of the running codespace and stop it.

![Open Codespace](/img/stop_codespace.png)

Read this guide as a <a href="quickstart.html">Slideshow</a>.

## Docker setup

This is the most effective solution to get a fully fledged dev environment (locally): with minimal installation requirements (just Docker) and full controll over the available resources, as well as over the whole environment!

Once installed [Docker](https://www.docker.com/) on you personal computer (check out the right installation package given the OS)

![Open Codespace](/img/docker_download.png)

open any CLI, and run the following command

    docker run --name snake-autoplay -d -p 8020-8040:8020-8040 alnoda/python-workspace

this will run a Docker container, in detached mode, with the promised dev environment accessible from the browser.

After the [alnoda/python-workspace](https://hub.docker.com/r/alnoda/python-workspace) Docker image has been pulled (the very first time) and the Docker container is up and running, go to [localhost:8020](http://localhost:8020/)

![Open Codespace](/img/docker_alnoda.png)

From there open the `Terminal` webapp (CLI) and there, clone the repo [andreagalle/snake-autoplay](https://github.com/andreagalle/snake-autoplay)

    git clone https://github.com/andreagalle/snake-autoplay.git

Let's start installing all the necessary dependecies, starting from `pygame` module, the most important one!

    pip install pygame

Then, let's install a custom version of the `pygbag` module:

    git clone https://github.com/andreagalle/pygbag.git
    cd pygbag
    git checkout docker-workspace
    pip install -e $PWD

Now go back to the root repo

    cd ../snake-autoplay/

from there deploy the game, as a webapp, with the following command:

    pygbag --docker_workspace --port 8030 main.py

go to [localhost:8030](http://localhost:8030/) click on the `Ready to start!` button, navigate the menu to choose the game mode and that's it!