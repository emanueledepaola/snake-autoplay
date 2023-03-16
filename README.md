# Quickstart Guide

Follow these simple steps to fire up a Linux host &ndash; with full control over it &ndash; and anything you need, just in a couple commands!

### TL;DR

- [GitHub Codespace setup](#github-codespace-setup)
- [Docker setup](#docker-setup)

If interested in understanding what's happening under the hood: in a few words, a containerized dev environment is instantiated in both cases (here below &ndash; locally, with Docker or in the cloud, on GitHub). From there, all the fundamental tools we need to develop (i.e. an IDE and the CLI), are accessible from the browser itself. 

What was missing was in principle just a GUI to to render `pygame` graphics.

To overcome this issue, fortunately thanks to the `pygbag` module, we can access the game as a webapp on a browser-based GUI. More info on this package at the following links:
- [Python Package](https://pypi.org/project/pygbag/)
- [Project Page](https://pygame-web.github.io/)
- [GitHub Repo](https://github.com/pygame-web/pygbag)

## GitHub Codespace setup 

This is the quickest way to spin up a lightweight dev environment (in the cloud) without the need of installing anything at all on your personal computer, althougth sacrifying to some extent the available resources and control, over the environment itself.

Once logged-in on [GitHub](https://github.com/), navigate to the repo [andreagalle/snake-autoplay](https://github.com/andreagalle/snake-autoplay) and click on the `Use this template > Open in a codespace` button 

![Open Codespace](https://raw.githubusercontent.com/andreagalle/snake-autoplay/focus-group-demo/img/open_codespace.png)

This will open a browser-based IDE (essentially vscode) in a new tab. As you instantiate this particular codespace, from the integrated CLI launch the setup script, after having sourced the hidden `.env` file:

    source .env
    setup

to install (first time only) all the dependecies we need, basically `pygame` and a custom version of `pygbag` modules.

Then, navigate to the snake version you want to run, for instance the standard one and launch the deploy script:

    cd std/
    deploy

this basically use `pygbag` module passing the GitHub `${CODESPACE_NAME}` environment variable, to deploy the game on that domain name (randomly choosed by GitHub itself), under the default port `8000`.

![Open Codespace](https://raw.githubusercontent.com/andreagalle/snake-autoplay/focus-group-demo/img/url_codespace.png)

This domain name must coincide with the string highlighted in the above URL thus, launching the deploy script would be the same as running the following command, for instance:

    pygbag --gh_codespace "animated-space-zebra" main.py

passing the `"animated-space-zebra"` codespace name itself, randomly assigned by GitHub itself. That's important to remember, just in case the `${CODESPACE_NAME}` environment variable won't work anymore in the future!

![Open Codespace](https://raw.githubusercontent.com/andreagalle/snake-autoplay/focus-group-demo/img/animated_space_zebra.png)
( *"An animated space zebra in the style of vector artwork."* asked to [DALL·E 2 - OpenAI](https://labs.openai.com/ ) the 16th March 2023.)

Now click on the `Ready to start!` button and that's it!

**N.B.** always remember to turn off the codespace we just instantiated, not to waste useful resources (i.e. core hours used). Thus click on the GitHub `Codespace` tab at the Top Navigation Bar of the repo

![Open Codespace](https://raw.githubusercontent.com/andreagalle/snake-autoplay/focus-group-demo/img/bar_codespace.png)

then, search for the (randomly generated) name of the running codespace and stop it.

![Open Codespace](https://raw.githubusercontent.com/andreagalle/snake-autoplay/focus-group-demo/img/stop_codespace.png)

## Docker setup

This is the most effective solution to get a fully fledged dev environment (locally): with minimal installation requirements (just Docker) and full controll over the available resources, as well as over the whole environment!

Once installed [Docker](https://www.docker.com/) on you personal computer (check out the right installation package given the OS)

![Open Codespace](https://raw.githubusercontent.com/andreagalle/snake-autoplay/focus-group-demo/img/docker_download.png)

open any CLI, and run the following command

    docker run --name snake-autoplay -d -p 8020-8040:8020-8040 alnoda/python-workspace

this will run a Docker container, in detached mode, with the promised dev environment accessible from the browser.

After the [alnoda/python-workspace](https://hub.docker.com/r/alnoda/python-workspace) Docker image has been pulled (the very first time) and the Docker container is up and running, go to [localhost:8020](http://localhost:8020/)

![Open Codespace](https://raw.githubusercontent.com/andreagalle/snake-autoplay/focus-group-demo/img/docker_alnoda.png)

From there open the `Terminal` webapp (CLI) and there, clone the repo [andreagalle/snake-autoplay](https://github.com/andreagalle/snake-autoplay)

    git clone https://github.com/andreagalle/snake-autoplay.git

Let's start installing all the necessary dependecies, starting from `pygame` module, the most important one!

    pip install pygame

Then, let's install a custom version of the `pygbag` module:

    git clone https://github.com/andreagalle/pygbag.git
    cd pygbag
    git checkout docker-workspace
    pip install -e $PWD

Now go back to the root repo and navigate to the snake version you want to run, for instance the standard one:

    cd ../snake-autoplay/
    cd std/

From there, deploy it with the following command

    pygbag --docker_workspace --port 8030 main.py

go to [localhost:8030](http://localhost:8030/) click on the `Ready to start!` button and that's it!