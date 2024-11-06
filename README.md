# VSCode Python Debug Bug

> Sample application to demonstrate an issue I'm facing with VSCode v1.92+.

## Background

This repository is me trying to create a simple example to reproduce a problem I'm facing with VSCode. One feature I take advantage of pretty extensively is debugging, specifically debugging tests. Unfortunately I've run into an issue recently where I've been unable to step into third party code while debugging test cases. I don't really know why. I tried tweaking a bunch of configuration settings in VSCode to see if I could get it to work with no such luck. So I'm creating this repo and submitting a bug with VSCode.

## Setup

Make sure to install the dependencies of the project with poetry and use the .venv folder for the interpreter with VSCode.

## Expected

![](https://github.com/user-attachments/assets/6aa91d7e-2978-41c4-bb10-f0f857fb3900)

With VSCode v1.91.x, when I try to step into the third party module it works.

## Actual

![](
https://github.com/user-attachments/assets/0bca4c4e-b447-4066-a216-71dcaa88c609)

With VSCode v1.92+ (including v1.95.x), when I try to step into the third party module it doesn't actually step in and continues the debugging session in my code.



