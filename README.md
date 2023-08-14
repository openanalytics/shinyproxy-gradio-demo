# Running Gradio apps inside ShinyProxy

This repository describes how to add a [Gradio](https://www.gradio.app/) app inside ShinyProxy (at least version 2.5.0) using [FastApi](https://fastapi.tiangolo.com/).

# Build the Docker image

To pull the image made in this repository from Docker Hub, use

```
sudo docker pull openanalytics/shinyproxy-gradio-demo
```

the relevant Docker Hub repository can be found at https://hub.docker.com/r/openanalytics/shinyproxy-gradio-demo

To build the image from the Dockerfile, clone this repository, then navigate to its root directory and run

```
sudo docker build -t openanalytics/shinyproxy-gradio-demo .
```

# ShinyProxy Configuration

To add the gradio application to ShinyProxy add the following lines to its configuration file (see [application.yml](./application.yml) for the complete file):

```yaml
specs:
  - id: gradio-demo
    display-name: Gradio Demo Application
    port: 8000
    container-image: gradio-demo
    target-path: "#{proxy.getRuntimeValue('SHINYPROXY_PUBLIC_PATH')}"
```

# References
* https://www.gradio.app/guides/quickstart
* https://github.com/gradio-app/gradio/issues/344#issuecomment-1247033951

**(c) Copyright Open Analytics NV, 2023.**
