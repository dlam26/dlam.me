/*
    ...because every decade the dlam.me foundation does a rebuild of its great website

    https://expressjs.com/en/starter/hello-world.html
    https://blog.logrocket.com/how-to-set-up-node-typescript-express/
    https://expressjs.com/en/api.html
 */
import express, { Express, Request, Response } from 'express';
import path from 'path';
import child_process from 'child_process';
const bodyParser = require('body-parser');

const app = express(), port = 3000

app.set('views', path.join(__dirname, 'expressjs/views'))
app.set('view engine', 'pug')
app.use(bodyParser.json());

const COWSAY_CMD = child_process.execSync('which cowsay')

const cowfiles = [
  "beavis.zen",
  "bong",
  "bud-frogs",
  "bunny",
  "cheese",
  "cower",
  "daemon",
  "default",
  "dragon-and-cow",
  "dragon",
  "elephant-in-snake",
  "elephant",
  // "eyes",
  "flaming-sheep",
  "ghostbusters",
  "head-in",
  "hellokitty",
  "kiss",
  "kitty",
  "koala",
  "kosh",
  "luke-koala",
  "mech-and-cow",
  "meow",
  "milk",
  "moofasa",
  "moose",
  "mutilated",
  "ren",
  "satanic",
  "sheep",
  "skeleton",
  "small",
  // "sodomized",
  "stegosaurus",
  "stimpy",
  "supermilker",
  "surgery",
  // "telebears",
  "three-eyes",
  "turkey",
  "turtle",
  "tux",
  "udder",
  "vader-koala",
  "vader",
  "www"
]

app.get('/', (req: Request, res: Response) => {
  // res.send('HELLO FROM app.ts:15!!!!')
  const WRAP_COL = 50

  var cowfile = cowfiles[Math.floor(Math.random() * cowfiles.length)]
  var cowsayOutput = child_process.execSync(`fortune | ${COWSAY_CMD} -W ${WRAP_COL} -f ${cowfile}`);

  res.render('homepage', {
    cowfile,
    cowsayOutput: cowsayOutput,
    someContextVar: 'O__O  (from app.ts:19) ',

  })
})

app.get('/get-cow', (req: Request, res: Response) => {

  let cmd = ''


  var cowsayOutput = child_process.execSync(cmd).toString();
  res.header("Access-Control-Allow-Origin", "*")    // via https://stackoverflow.com/questions/43362431/
  res.header("Access-Control-Allow-Credentials", "true")
  res.json({
    cowsay: "TODO FIXME",
    cowsayOutput: cowsayOutput,
  })
})

app.listen(port, () => {
  console.log(`dlam.me backend listening on port ${port}...  :D`)
})

// vi: sw=2
