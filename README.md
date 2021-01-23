<h1 align="center">Welcome to socketio-cli 👋</h1>
<p align="center">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dw/socketio-cli">
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/socketio-cli?style=flat-square">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/socketio-cli">
</p>

> A command-line client for socket.io, websocket, unix-socket that has auto-completion and syntax highlighting.

This project was created from [socket-cli](https://github.com/gcaaa31928/socket-cli).

## ✨ Demo

### Just take a look
[![asciicast](https://asciinema.org/a/GgXCsrUEhlY98xxlrhIQcRpNj.svg)](https://asciinema.org/a/GgXCsrUEhlY98xxlrhIQcRpNj?speed=2)

## 🚀 Usage

install *socketio-cli* via pip:

```bash
pip install socketio-cli
```
```bash
Usage: socketio-cli [OPTIONS] [PATH]

Options:
  -t, --type TEXT  [websocket, socketio, unix]
  --help           Show this message and exit.
````

when you connect a socket.io server.
```bash
> connect
> emit --event event_name --data '{"test": "data"}'
> on --event event_name
> on --event event_name --namespace /admin
> emit --event event_name --data '{"test": "data"}' --namespace /admin
```
or a websocket server
```bash
> connect
> send --data test
> recv
```
or a unix socket server
```bash
> connect
> send --data test
```

```bash
> connect
> send --data
> on --event event_name
```

## 🤝 Contributing

Contributions, issues and feature requests are welcome.<br />
Feel free to check [issues page](https://github.com/gcaaa31928/socketio-cli/issues) and pull-request welcome.
