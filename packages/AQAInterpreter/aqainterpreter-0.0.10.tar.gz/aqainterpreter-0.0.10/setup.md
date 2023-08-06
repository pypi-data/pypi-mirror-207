## packages needed for development in ubuntu code-space or local fedora workstation
```bash
# ubuntu
sudo apt update && sudo apt upgrade -y
sudo apt install hatch pandoc texlive-xetex fonts-firacode yarnpkg fossil entr -y

# fedora
sudo dnf install hatch pandoc texlive-xetex fira-code-fonts yarnpkg librsvg2-tools texlive-scheme-medium fossil entr -y
```

## building flowcharts
```bash
# https://github.com/mermaid-js/mermaid-cli#install-locally
sudo yarn global add -g @mermaid-js/mermaid-cli
# then manually change `==` to `<=` for syntax_tree.svg with inspect element
# because otherwise renders as `&lt;`
# auto generate packages.mmd and classes.md
pyreverse ./AQAInterpreter/ -o mmd
```

## setup project
```bash
hatch shell

# publish to pypi
# increment version in `pyproject.toml`
hatch build && hatch publish && rm -rf dist
  # running this command for the first time requires token from https://pypi.org/help/#apitoken
```

## updating css in websites
```bash
npm install monaco-editor
# manually drag out `vs` folder and place in static/
curl https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css -o website/static/bootstrap.min.css
curl https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/fonts/bootstrap-icons.woff2 -o website/static/bootstrap-icons.woff2
curl https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.min.css -o website/static/bootstrap-icons.min.css
```

## deploying on ec2

first setup apache2 as a reverse proxy by following https://www.digitalocean.com/community/tutorials/how-to-use-apache-http-server-as-reverse-proxy-using-mod_proxy-extension-ubuntu-20-04

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3-pip
pip install hatchling
git clone https://github.com/CyberWarrior5466/nea.git
cd nea
/ubuntu/.local/bin/hatch shell
uvicorn website.app:app
```