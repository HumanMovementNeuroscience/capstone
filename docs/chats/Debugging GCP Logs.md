# Debugging GCP Logs

+++++++++++++++++

LOGS FROM A WORKING DEPLOYMENT START
2024-01-03T02:29:53.7614146Z Requested labels: ubuntu-latest
2024-01-03T02:29:53.7614470Z Job defined at: freemocap/skellybot/.github/workflows/google-cloudrun-docker.yml@refs/heads/main
2024-01-03T02:29:53.7614583Z Waiting for a runner to pick up this job...
2024-01-03T02:29:54.2561592Z Job is waiting for a hosted runner to come online.
2024-01-03T02:29:56.6453920Z Job is about to start running on the hosted runner: GitHub Actions 3 (hosted)
2024-01-03T02:29:59.5656315Z Current runner version: '2.311.0'
2024-01-03T02:29:59.5679991Z ##[group]Operating System
2024-01-03T02:29:59.5680625Z Ubuntu
2024-01-03T02:29:59.5680976Z 22.04.3
2024-01-03T02:29:59.5681406Z LTS
2024-01-03T02:29:59.5681748Z ##[endgroup]
2024-01-03T02:29:59.5682144Z ##[group]Runner Image
2024-01-03T02:29:59.5682613Z Image: ubuntu-22.04
2024-01-03T02:29:59.5683041Z Version: 20231217.2.0
2024-01-03T02:29:59.5684045Z Included Software: https://github.com/actions/runner-images/blob/ubuntu22/20231217.2/images/ubuntu/Ubuntu2204-Readme.md
2024-01-03T02:29:59.5685560Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu22%2F20231217.2
2024-01-03T02:29:59.5686470Z ##[endgroup]
2024-01-03T02:29:59.5686929Z ##[group]Runner Image Provisioner
2024-01-03T02:29:59.5687377Z 2.0.321.1
2024-01-03T02:29:59.5687731Z ##[endgroup]
2024-01-03T02:29:59.5688636Z ##[group]GITHUB_TOKEN Permissions
2024-01-03T02:29:59.5690238Z Contents: read
2024-01-03T02:29:59.5690645Z Metadata: read
2024-01-03T02:29:59.5691568Z ##[endgroup]
2024-01-03T02:29:59.5695173Z Secret source: Actions
2024-01-03T02:29:59.5695768Z Prepare workflow directory
2024-01-03T02:29:59.6441894Z Prepare all required actions
2024-01-03T02:29:59.6599229Z Getting action download info
2024-01-03T02:29:59.8945647Z Download action repository 'actions/checkout@v4' (SHA:b4ffde65f46336ab88eb53be808477a3936bae11)
2024-01-03T02:29:59.9994072Z Download action repository 'google-github-actions/auth@v2' (SHA:67e9c72af6e0492df856527b474995862b7b6591)
2024-01-03T02:30:00.3809052Z Download action repository 'docker/login-action@v3' (SHA:343f7c4344506bcbf9b4de18042ae17996df046d)
2024-01-03T02:30:00.8510897Z Complete job name: deploy
2024-01-03T02:30:00.9447399Z ##[group]Run actions/checkout@v4
2024-01-03T02:30:00.9447994Z with:
2024-01-03T02:30:00.9448431Z   repository: freemocap/skellybot
2024-01-03T02:30:00.9449317Z   token: ***
2024-01-03T02:30:00.9449741Z   ssh-strict: true
2024-01-03T02:30:00.9450280Z   persist-credentials: true
2024-01-03T02:30:00.9450779Z   clean: true
2024-01-03T02:30:00.9451196Z   sparse-checkout-cone-mode: true
2024-01-03T02:30:00.9451825Z   fetch-depth: 1
2024-01-03T02:30:00.9452237Z   fetch-tags: false
2024-01-03T02:30:00.9452689Z   show-progress: true
2024-01-03T02:30:00.9453198Z   lfs: false
2024-01-03T02:30:00.9453580Z   submodules: false
2024-01-03T02:30:00.9454011Z   set-safe-directory: true
2024-01-03T02:30:00.9454762Z env:
2024-01-03T02:30:00.9455177Z   PROJECT_ID: mocap-test-project
2024-01-03T02:30:00.9455741Z   GAR_LOCATION: us-east1
2024-01-03T02:30:00.9456280Z   SERVICE: jonbot/nestbot
2024-01-03T02:30:00.9456727Z   REGION: us-central1
2024-01-03T02:30:00.9457153Z ##[endgroup]
2024-01-03T02:30:01.1123271Z Syncing repository: freemocap/skellybot
2024-01-03T02:30:01.1126047Z ##[group]Getting Git version info
2024-01-03T02:30:01.1127407Z Working directory is '/home/runner/work/skellybot/skellybot'
2024-01-03T02:30:01.1129229Z [command]/usr/bin/git version
2024-01-03T02:30:01.1130071Z git version 2.43.0
2024-01-03T02:30:01.1138783Z ##[endgroup]
2024-01-03T02:30:01.1156178Z Temporarily overriding HOME='/home/runner/work/_temp/8e322c3b-8ac5-4670-91c4-8931b19ebe76' before making global git config changes
2024-01-03T02:30:01.1158675Z Adding repository directory to the temporary git global config as a safe directory
2024-01-03T02:30:01.1161040Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/skellybot/skellybot
2024-01-03T02:30:01.1193313Z Deleting the contents of '/home/runner/work/skellybot/skellybot'
2024-01-03T02:30:01.1198826Z ##[group]Initializing the repository
2024-01-03T02:30:01.1201721Z [command]/usr/bin/git init /home/runner/work/skellybot/skellybot
2024-01-03T02:30:01.1292342Z hint: Using 'master' as the name for the initial branch. This default branch name
2024-01-03T02:30:01.1294208Z hint: is subject to change. To configure the initial branch name to use in all
2024-01-03T02:30:01.1295559Z hint: of your new repositories, which will suppress this warning, call:
2024-01-03T02:30:01.1296498Z hint: 
2024-01-03T02:30:01.1297388Z hint: 	git config --global init.defaultBranch <name>
2024-01-03T02:30:01.1298143Z hint: 
2024-01-03T02:30:01.1298945Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2024-01-03T02:30:01.1300099Z hint: 'development'. The just-created branch can be renamed via this command:
2024-01-03T02:30:01.1301021Z hint: 
2024-01-03T02:30:01.1301474Z hint: 	git branch -m <name>
2024-01-03T02:30:01.1308816Z Initialized empty Git repository in /home/runner/work/skellybot/skellybot/.git/
2024-01-03T02:30:01.1317469Z [command]/usr/bin/git remote add origin https://github.com/freemocap/skellybot
2024-01-03T02:30:01.1354496Z ##[endgroup]
2024-01-03T02:30:01.1355344Z ##[group]Disabling automatic garbage collection
2024-01-03T02:30:01.1356756Z [command]/usr/bin/git config --local gc.auto 0
2024-01-03T02:30:01.1385198Z ##[endgroup]
2024-01-03T02:30:01.1385958Z ##[group]Setting up auth
2024-01-03T02:30:01.1389979Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2024-01-03T02:30:01.1418497Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2024-01-03T02:30:01.1760124Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2024-01-03T02:30:01.1787919Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2024-01-03T02:30:01.2018640Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2024-01-03T02:30:01.2051175Z ##[endgroup]
2024-01-03T02:30:01.2052201Z ##[group]Fetching the repository
2024-01-03T02:30:01.2064032Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +676f2b55cf418a17d13170730d6e74fdec198dea:refs/remotes/origin/main
2024-01-03T02:30:01.7113362Z From https://github.com/freemocap/skellybot
2024-01-03T02:30:01.7114390Z  * [new ref]         676f2b55cf418a17d13170730d6e74fdec198dea -> origin/main
2024-01-03T02:30:01.7142315Z ##[endgroup]
2024-01-03T02:30:01.7143428Z ##[group]Determining the checkout info
2024-01-03T02:30:01.7144804Z ##[endgroup]
2024-01-03T02:30:01.7145806Z ##[group]Checking out the ref
2024-01-03T02:30:01.7150092Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2024-01-03T02:30:01.7893649Z Switched to a new branch 'main'
2024-01-03T02:30:01.7895770Z branch 'main' set up to track 'origin/main'.
2024-01-03T02:30:01.7905912Z ##[endgroup]
2024-01-03T02:30:01.7944731Z [command]/usr/bin/git log -1 --format='%H'
2024-01-03T02:30:01.7968849Z '676f2b55cf418a17d13170730d6e74fdec198dea'
2024-01-03T02:30:01.8296540Z ##[group]Run google-github-actions/auth@v2
2024-01-03T02:30:01.8297068Z with:
2024-01-03T02:30:01.8297440Z   project_id: mocap-test-project
2024-01-03T02:30:01.8297975Z   token_format: access_token
2024-01-03T02:30:01.8299159Z   workload_identity_provider: ***
2024-01-03T02:30:01.8299977Z   service_account: ***
2024-01-03T02:30:01.8300373Z   create_credentials_file: true
2024-01-03T02:30:01.8300924Z   export_environment_variables: true
2024-01-03T02:30:01.8301355Z   universe: googleapis.com
2024-01-03T02:30:01.8301720Z   cleanup_credentials: true
2024-01-03T02:30:01.8302114Z   access_token_lifetime: 3600s
2024-01-03T02:30:01.8302654Z   access_token_scopes: https://www.googleapis.com/auth/cloud-platform
2024-01-03T02:30:01.8303271Z   retries: 3
2024-01-03T02:30:01.8303589Z   backoff: 250
2024-01-03T02:30:01.8303949Z   id_token_include_email: false
2024-01-03T02:30:01.8304370Z env:
2024-01-03T02:30:01.8304694Z   PROJECT_ID: mocap-test-project
2024-01-03T02:30:01.8305289Z   GAR_LOCATION: us-east1
2024-01-03T02:30:01.8305662Z   SERVICE: jonbot/nestbot
2024-01-03T02:30:01.8306011Z   REGION: us-central1
2024-01-03T02:30:01.8306409Z ##[endgroup]
2024-01-03T02:30:02.0683904Z Created credentials file at "/home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json"
2024-01-03T02:30:02.3122620Z ##[group]Run docker/login-action@v3
2024-01-03T02:30:02.3123133Z with:
2024-01-03T02:30:02.3123565Z   username: oauth2accesstoken
2024-01-03T02:30:02.3129361Z   password: ***
2024-01-03T02:30:02.3129757Z   registry: us-east1-docker.pkg.dev
2024-01-03T02:30:02.3130248Z   ecr: auto
2024-01-03T02:30:02.3130593Z   logout: true
2024-01-03T02:30:02.3130985Z env:
2024-01-03T02:30:02.3131336Z   PROJECT_ID: mocap-test-project
2024-01-03T02:30:02.3131967Z   GAR_LOCATION: us-east1
2024-01-03T02:30:02.3132515Z   SERVICE: jonbot/nestbot
2024-01-03T02:30:02.3132917Z   REGION: us-central1
2024-01-03T02:30:02.3133615Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:02.3135282Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:02.3136408Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:02.3137352Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-03T02:30:02.3137844Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-03T02:30:02.3138352Z   GCLOUD_PROJECT: mocap-test-project
2024-01-03T02:30:02.3138811Z   GCP_PROJECT: mocap-test-project
2024-01-03T02:30:02.3139254Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-03T02:30:02.3139770Z ##[endgroup]
2024-01-03T02:30:02.4143911Z Logging into us-east1-docker.pkg.dev...
2024-01-03T02:30:03.1215891Z Login Succeeded!
2024-01-03T02:30:03.1328630Z ##[group]Run docker build -t "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:676f2b55cf418a17d13170730d6e74fdec198dea" ./
2024-01-03T02:30:03.1330041Z [36;1mdocker build -t "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:676f2b55cf418a17d13170730d6e74fdec198dea" ./[0m
2024-01-03T02:30:03.1331288Z [36;1mdocker build -t "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:latest" ./[0m
2024-01-03T02:30:03.1332362Z [36;1mdocker push "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:676f2b55cf418a17d13170730d6e74fdec198dea"[0m
2024-01-03T02:30:03.1333390Z [36;1mdocker push "us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:latest"[0m
2024-01-03T02:30:03.1398166Z shell: /usr/bin/bash -e {0}
2024-01-03T02:30:03.1398614Z env:
2024-01-03T02:30:03.1398957Z   PROJECT_ID: mocap-test-project
2024-01-03T02:30:03.1399454Z   GAR_LOCATION: us-east1
2024-01-03T02:30:03.1399899Z   SERVICE: jonbot/nestbot
2024-01-03T02:30:03.1400383Z   REGION: us-central1
2024-01-03T02:30:03.1401134Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:03.1402157Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:03.1403170Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:30:03.1403861Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-03T02:30:03.1404425Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-03T02:30:03.1404914Z   GCLOUD_PROJECT: mocap-test-project
2024-01-03T02:30:03.1405342Z   GCP_PROJECT: mocap-test-project
2024-01-03T02:30:03.1405869Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-03T02:30:03.1406307Z ##[endgroup]
2024-01-03T02:30:03.5675877Z #0 building with "default" instance using docker driver
2024-01-03T02:30:03.5677115Z 
2024-01-03T02:30:03.5680802Z #1 [internal] load build definition from Dockerfile
2024-01-03T02:30:03.5681712Z #1 transferring dockerfile: 1.03kB done
2024-01-03T02:30:03.5682574Z #1 DONE 0.0s
2024-01-03T02:30:03.5682807Z 
2024-01-03T02:30:03.5683055Z #2 [internal] load .dockerignore
2024-01-03T02:30:03.5684375Z #2 transferring context: 57B done
2024-01-03T02:30:03.5685131Z #2 DONE 0.0s
2024-01-03T02:30:03.5685465Z 
2024-01-03T02:30:03.5686139Z #3 [auth] docker/dockerfile:pull token for registry-1.docker.io
2024-01-03T02:30:03.5687136Z #3 DONE 0.0s
2024-01-03T02:30:03.5687807Z 
2024-01-03T02:30:03.5688186Z #4 resolve image config for docker.io/docker/dockerfile:1.2
2024-01-03T02:30:04.7706417Z #4 DONE 1.3s
2024-01-03T02:30:04.7706835Z 
2024-01-03T02:30:04.7707888Z #5 docker-image://docker.io/docker/dockerfile:1.2@sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc
2024-01-03T02:30:04.7709381Z #5 resolve docker.io/docker/dockerfile:1.2@sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc done
2024-01-03T02:30:04.8953859Z #5 sha256:86e43bba076d67c1a890cbc07813806b11eca53843dc643202d939b986c8c332 1.21kB / 1.21kB done
2024-01-03T02:30:04.8955766Z #5 sha256:3cc8e449ce9f6e0752ede8f50a7334bf0c7b2d24d76da2ffae7aa6a729dd1da4 9.64MB / 9.64MB 0.2s done
2024-01-03T02:30:04.8957452Z #5 sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc 1.69kB / 1.69kB done
2024-01-03T02:30:04.8959009Z #5 sha256:e3ee2e6b536452d876b1c5aa12db9bca51b8f52b2505178cae6d13e33daeed2b 528B / 528B done
2024-01-03T02:30:04.8960581Z #5 extracting sha256:3cc8e449ce9f6e0752ede8f50a7334bf0c7b2d24d76da2ffae7aa6a729dd1da4
2024-01-03T02:30:05.0450864Z #5 extracting sha256:3cc8e449ce9f6e0752ede8f50a7334bf0c7b2d24d76da2ffae7aa6a729dd1da4 0.1s done
2024-01-03T02:30:05.0451847Z #5 DONE 0.3s
2024-01-03T02:30:05.1957540Z 
2024-01-03T02:30:05.1959197Z #6 [internal] load .dockerignore
2024-01-03T02:30:05.1960100Z #6 DONE 0.0s
2024-01-03T02:30:05.1960377Z 
2024-01-03T02:30:05.1960659Z #7 [internal] load build definition from Dockerfile
2024-01-03T02:30:05.1961364Z #7 DONE 0.0s
2024-01-03T02:30:05.1961621Z 
2024-01-03T02:30:05.1962522Z #8 [auth] library/node:pull token for registry-1.docker.io
2024-01-03T02:30:05.1963205Z #8 DONE 0.0s
2024-01-03T02:30:05.1963560Z 
2024-01-03T02:30:05.1963987Z #9 [internal] load metadata for docker.io/library/node:20.10.0-slim
2024-01-03T02:30:05.4801757Z #9 DONE 0.4s
2024-01-03T02:30:05.6301975Z 
2024-01-03T02:30:05.6304741Z #10 [stage-0  1/12] FROM docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6
2024-01-03T02:30:05.6307537Z #10 resolve docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6 done
2024-01-03T02:30:05.7402719Z #10 ...
2024-01-03T02:30:05.7403008Z 
2024-01-03T02:30:05.7403249Z #11 [internal] load build context
2024-01-03T02:30:05.7404120Z #11 transferring context: 20.31MB 0.2s done
2024-01-03T02:30:05.7404618Z #11 DONE 0.2s
2024-01-03T02:30:05.7404800Z 
2024-01-03T02:30:05.7405790Z #10 [stage-0  1/12] FROM docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6
2024-01-03T02:30:05.7406930Z #10 sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6 1.21kB / 1.21kB done
2024-01-03T02:30:05.7407874Z #10 sha256:df49e2dc50b7b1f91b44201432cefaf034f66e549bcbd3a29745ffff439afc9e 1.37kB / 1.37kB done
2024-01-03T02:30:05.7408881Z #10 sha256:03f4750834334638efe8f99b5b6c69c08048988fe711078c6889d536dc88aea1 7.62kB / 7.62kB done
2024-01-03T02:30:05.7409821Z #10 sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81 14.68MB / 29.13MB 0.2s
2024-01-03T02:30:05.7410758Z #10 sha256:ebd7ac832a7e4bd07f5ad6f4bbc6db1f5b02de7a8e07b40627142ef61a9b1b9d 0B / 3.36kB 0.2s
2024-01-03T02:30:05.7411769Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 3.15MB / 40.46MB 0.2s
2024-01-03T02:30:05.8436453Z #10 sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81 28.31MB / 29.13MB 0.3s
2024-01-03T02:30:05.8438267Z #10 sha256:ebd7ac832a7e4bd07f5ad6f4bbc6db1f5b02de7a8e07b40627142ef61a9b1b9d 3.36kB / 3.36kB 0.2s done
2024-01-03T02:30:05.8440073Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 14.68MB / 40.46MB 0.3s
2024-01-03T02:30:05.8441826Z #10 sha256:e21beee6f6d33b4605828c995958d12a7fb3762621c15d3c4355bfed122a11f0 0B / 2.67MB 0.3s
2024-01-03T02:30:05.9942847Z #10 sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81 29.13MB / 29.13MB 0.3s done
2024-01-03T02:30:05.9946843Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 29.36MB / 40.46MB 0.4s
2024-01-03T02:30:05.9948296Z #10 sha256:e21beee6f6d33b4605828c995958d12a7fb3762621c15d3c4355bfed122a11f0 2.67MB / 2.67MB 0.3s done
2024-01-03T02:30:05.9950738Z #10 extracting sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81
2024-01-03T02:30:05.9952239Z #10 sha256:6e2165efc3a7fb15942e607201f825c49ec4b664e3988e01e2e4a78b682da50e 451B / 451B 0.4s done
2024-01-03T02:30:06.1280381Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 32.51MB / 40.46MB 0.5s
2024-01-03T02:30:06.2310865Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 39.85MB / 40.46MB 0.6s
2024-01-03T02:30:06.4834103Z #10 sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 40.46MB / 40.46MB 0.8s done
2024-01-03T02:30:07.0468504Z #10 extracting sha256:af107e978371b6cd6339127a05502c5eacd1e6b0e9eb7b2f4aa7b6fc87e2dd81 1.1s done
2024-01-03T02:30:07.0470374Z #10 extracting sha256:ebd7ac832a7e4bd07f5ad6f4bbc6db1f5b02de7a8e07b40627142ef61a9b1b9d done
2024-01-03T02:30:07.0472008Z #10 extracting sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281
2024-01-03T02:30:08.3706187Z #10 extracting sha256:c5da3822f0fa5def8cc49ddb050ab51e134b313fe72ac31489d0303587f27281 1.2s done
2024-01-03T02:30:08.4996516Z #10 extracting sha256:e21beee6f6d33b4605828c995958d12a7fb3762621c15d3c4355bfed122a11f0 0.1s done
2024-01-03T02:30:08.6500595Z #10 extracting sha256:6e2165efc3a7fb15942e607201f825c49ec4b664e3988e01e2e4a78b682da50e done
2024-01-03T02:30:08.6501707Z #10 DONE 3.0s
2024-01-03T02:30:08.6501958Z 
2024-01-03T02:30:08.6502464Z #12 [stage-0  2/12] WORKDIR /workspace
2024-01-03T02:30:08.6502928Z #12 DONE 0.0s
2024-01-03T02:30:08.6503157Z 
2024-01-03T02:30:08.6503463Z #13 [stage-0  3/12] RUN rm -rf /etc/apt/apt.conf.d/docker-clean
2024-01-03T02:30:08.7723124Z #13 DONE 0.2s
2024-01-03T02:30:08.9230362Z 
2024-01-03T02:30:08.9231550Z #14 [stage-0  4/12] COPY ./bin/builds/ .
2024-01-03T02:30:08.9232476Z #14 DONE 0.0s
2024-01-03T02:30:08.9232796Z 
2024-01-03T02:30:08.9233196Z #15 [stage-0  5/12] RUN mkdir /home/.npm
2024-01-03T02:30:09.0755519Z #15 DONE 0.2s
2024-01-03T02:30:09.0755920Z 
2024-01-03T02:30:09.0757098Z #16 [stage-0  6/12] RUN useradd -m appuser && chown -R appuser /workspace && chown -R appuser "/home/.npm"
2024-01-03T02:30:09.3744536Z #16 DONE 0.2s
2024-01-03T02:30:09.3744988Z 
2024-01-03T02:30:09.3747152Z #17 [stage-0  7/12] RUN --mount=type=cache,target=/var/cache/apt ./install_packages     dumb-init     htop     make     g++     python3
2024-01-03T02:30:11.0133189Z #17 1.689 Reading package lists...
2024-01-03T02:30:11.0134028Z #17 1.699 Building dependency tree...
2024-01-03T02:30:11.1636164Z #17 1.778 Reading state information...
2024-01-03T02:30:11.1637176Z #17 1.873 The following additional packages will be installed:
2024-01-03T02:30:11.1638927Z #17 1.873   binutils binutils-common binutils-x86-64-linux-gnu cpp cpp-12 g++-12 gcc
2024-01-03T02:30:11.1640512Z #17 1.873   gcc-12 libasan8 libatomic1 libbinutils libc-dev-bin libc6-dev libcc1-0
2024-01-03T02:30:11.1641952Z #17 1.873   libcrypt-dev libctf-nobfd0 libctf0 libexpat1 libgcc-12-dev libgomp1
2024-01-03T02:30:11.1643196Z #17 1.873   libgprofng0 libgssapi-krb5-2 libisl23 libitm1 libjansson4 libk5crypto3
2024-01-03T02:30:11.1644382Z #17 1.873   libkeyutils1 libkrb5-3 libkrb5support0 liblsan0 libmpc3 libmpfr6
2024-01-03T02:30:11.1645737Z #17 1.873   libncursesw6 libnl-3-200 libnl-genl-3-200 libnsl-dev libnsl2
2024-01-03T02:30:11.1647267Z #17 1.873   libpython3-stdlib libpython3.11-minimal libpython3.11-stdlib libquadmath0
2024-01-03T02:30:11.1648652Z #17 1.873   libreadline8 libsqlite3-0 libssl3 libstdc++-12-dev libtirpc-common
2024-01-03T02:30:11.1649727Z #17 1.874   libtirpc-dev libtirpc3 libtsan2 libubsan1 linux-libc-dev media-types
2024-01-03T02:30:11.1651310Z #17 1.874   python3-minimal python3.11 python3.11-minimal readline-common rpcsvc-proto
2024-01-03T02:30:11.1652404Z #17 1.874 Suggested packages:
2024-01-03T02:30:11.1654566Z #17 1.874   binutils-doc cpp-doc gcc-12-locales cpp-12-doc g++-multilib g++-12-multilib
2024-01-03T02:30:11.1656134Z #17 1.874   gcc-12-doc gcc-multilib manpages-dev autoconf automake libtool flex bison
2024-01-03T02:30:11.1657735Z #17 1.874   gdb gcc-doc gcc-12-multilib lm-sensors lsof strace glibc-doc krb5-doc
2024-01-03T02:30:11.1659219Z #17 1.874   krb5-user libstdc++-12-doc make-doc python3-doc python3-tk python3-venv
2024-01-03T02:30:11.1660276Z #17 1.874   python3.11-venv python3.11-doc binfmt-support readline-doc
2024-01-03T02:30:11.1661363Z #17 1.874 Recommended packages:
2024-01-03T02:30:11.1662512Z #17 1.874   manpages manpages-dev libc-devtools krb5-locales libgpm2 ca-certificates
2024-01-03T02:30:11.4648652Z #17 2.133 The following NEW packages will be installed:
2024-01-03T02:30:11.4650122Z #17 2.133   binutils binutils-common binutils-x86-64-linux-gnu cpp cpp-12 dumb-init g++
2024-01-03T02:30:11.4651261Z #17 2.133   g++-12 gcc gcc-12 htop libasan8 libatomic1 libbinutils libc-dev-bin
2024-01-03T02:30:11.4652223Z #17 2.133   libc6-dev libcc1-0 libcrypt-dev libctf-nobfd0 libctf0 libexpat1
2024-01-03T02:30:11.4653118Z #17 2.133   libgcc-12-dev libgomp1 libgprofng0 libgssapi-krb5-2 libisl23 libitm1
2024-01-03T02:30:11.4654099Z #17 2.133   libjansson4 libk5crypto3 libkeyutils1 libkrb5-3 libkrb5support0 liblsan0
2024-01-03T02:30:11.4655266Z #17 2.133   libmpc3 libmpfr6 libncursesw6 libnl-3-200 libnl-genl-3-200 libnsl-dev
2024-01-03T02:30:11.4656231Z #17 2.133   libnsl2 libpython3-stdlib libpython3.11-minimal libpython3.11-stdlib
2024-01-03T02:30:11.4657365Z #17 2.133   libquadmath0 libreadline8 libsqlite3-0 libssl3 libstdc++-12-dev
2024-01-03T02:30:11.4658328Z #17 2.133   libtirpc-common libtirpc-dev libtirpc3 libtsan2 libubsan1 linux-libc-dev
2024-01-03T02:30:11.4659371Z #17 2.134   make media-types python3 python3-minimal python3.11 python3.11-minimal
2024-01-03T02:30:11.4660095Z #17 2.134   readline-common rpcsvc-proto
2024-01-03T02:30:11.4660768Z #17 2.173 0 upgraded, 62 newly installed, 0 to remove and 0 not upgraded.
2024-01-03T02:30:11.4661412Z #17 2.173 Need to get 73.0 MB of archives.
2024-01-03T02:30:11.4662016Z #17 2.173 After this operation, 294 MB of additional disk space will be used.
2024-01-03T02:30:11.4663035Z #17 2.173 Get:1 http://deb.debian.org/debian bookworm/main amd64 libssl3 amd64 3.0.11-1~deb12u2 [2019 kB]
2024-01-03T02:30:11.5657225Z #17 2.256 Get:2 http://deb.debian.org/debian bookworm/main amd64 libpython3.11-minimal amd64 3.11.2-6 [813 kB]
2024-01-03T02:30:11.5659369Z #17 2.260 Get:3 http://deb.debian.org/debian bookworm/main amd64 libexpat1 amd64 2.5.0-1 [99.3 kB]
2024-01-03T02:30:11.5661218Z #17 2.263 Get:4 http://deb.debian.org/debian bookworm/main amd64 python3.11-minimal amd64 3.11.2-6 [2064 kB]
2024-01-03T02:30:11.5663189Z #17 2.273 Get:5 http://deb.debian.org/debian bookworm/main amd64 python3-minimal amd64 3.11.2-1+b1 [26.3 kB]
2024-01-03T02:30:11.5664995Z #17 2.273 Get:6 http://deb.debian.org/debian bookworm/main amd64 media-types all 10.0.0 [26.1 kB]
2024-01-03T02:30:11.5666497Z #17 2.273 Get:7 http://deb.debian.org/debian bookworm/main amd64 libncursesw6 amd64 6.4-4 [134 kB]
2024-01-03T02:30:11.5668170Z #17 2.274 Get:8 http://deb.debian.org/debian bookworm/main amd64 libkrb5support0 amd64 1.20.1-2+deb12u1 [32.4 kB]
2024-01-03T02:30:11.5670013Z #17 2.274 Get:9 http://deb.debian.org/debian bookworm/main amd64 libk5crypto3 amd64 1.20.1-2+deb12u1 [78.9 kB]
2024-01-03T02:30:11.5671198Z #17 2.275 Get:10 http://deb.debian.org/debian bookworm/main amd64 libkeyutils1 amd64 1.6.3-2 [8808 B]
2024-01-03T02:30:11.5672973Z #17 2.275 Get:11 http://deb.debian.org/debian bookworm/main amd64 libkrb5-3 amd64 1.20.1-2+deb12u1 [332 kB]
2024-01-03T02:30:11.5674978Z #17 2.280 Get:12 http://deb.debian.org/debian bookworm/main amd64 libgssapi-krb5-2 amd64 1.20.1-2+deb12u1 [134 kB]
2024-01-03T02:30:11.5676845Z #17 2.281 Get:13 http://deb.debian.org/debian bookworm/main amd64 libtirpc-common all 1.3.3+ds-1 [14.0 kB]
2024-01-03T02:30:11.5678819Z #17 2.292 Get:14 http://deb.debian.org/debian bookworm/main amd64 libtirpc3 amd64 1.3.3+ds-1 [85.2 kB]
2024-01-03T02:30:11.5680811Z #17 2.293 Get:15 http://deb.debian.org/debian bookworm/main amd64 libnsl2 amd64 1.3.0-2 [39.5 kB]
2024-01-03T02:30:11.5682690Z #17 2.294 Get:16 http://deb.debian.org/debian bookworm/main amd64 readline-common all 8.2-1.3 [69.0 kB]
2024-01-03T02:30:11.5684511Z #17 2.295 Get:17 http://deb.debian.org/debian bookworm/main amd64 libreadline8 amd64 8.2-1.3 [166 kB]
2024-01-03T02:30:11.5686252Z #17 2.296 Get:18 http://deb.debian.org/debian bookworm/main amd64 libsqlite3-0 amd64 3.40.1-2 [837 kB]
2024-01-03T02:30:11.5688258Z #17 2.300 Get:19 http://deb.debian.org/debian bookworm/main amd64 libpython3.11-stdlib amd64 3.11.2-6 [1796 kB]
2024-01-03T02:30:11.5690100Z #17 2.307 Get:20 http://deb.debian.org/debian bookworm/main amd64 python3.11 amd64 3.11.2-6 [572 kB]
2024-01-03T02:30:11.5691918Z #17 2.310 Get:21 http://deb.debian.org/debian bookworm/main amd64 libpython3-stdlib amd64 3.11.2-1+b1 [9312 B]
2024-01-03T02:30:11.5693912Z #17 2.310 Get:22 http://deb.debian.org/debian bookworm/main amd64 python3 amd64 3.11.2-1+b1 [26.3 kB]
2024-01-03T02:30:11.5696035Z #17 2.310 Get:23 http://deb.debian.org/debian bookworm/main amd64 binutils-common amd64 2.40-2 [2487 kB]
2024-01-03T02:30:11.5697911Z #17 2.321 Get:24 http://deb.debian.org/debian bookworm/main amd64 libbinutils amd64 2.40-2 [572 kB]
2024-01-03T02:30:11.5699713Z #17 2.323 Get:25 http://deb.debian.org/debian bookworm/main amd64 libctf-nobfd0 amd64 2.40-2 [153 kB]
2024-01-03T02:30:11.5701652Z #17 2.324 Get:26 http://deb.debian.org/debian bookworm/main amd64 libctf0 amd64 2.40-2 [89.8 kB]
2024-01-03T02:30:11.5703481Z #17 2.325 Get:27 http://deb.debian.org/debian bookworm/main amd64 libgprofng0 amd64 2.40-2 [812 kB]
2024-01-03T02:30:11.5705276Z #17 2.328 Get:28 http://deb.debian.org/debian bookworm/main amd64 libjansson4 amd64 2.14-2 [40.8 kB]
2024-01-03T02:30:11.5707250Z #17 2.331 Get:29 http://deb.debian.org/debian bookworm/main amd64 binutils-x86-64-linux-gnu amd64 2.40-2 [2246 kB]
2024-01-03T02:30:11.6660906Z #17 2.341 Get:30 http://deb.debian.org/debian bookworm/main amd64 binutils amd64 2.40-2 [65.0 kB]
2024-01-03T02:30:11.6663999Z #17 2.341 Get:31 http://deb.debian.org/debian bookworm/main amd64 libisl23 amd64 0.25-1 [690 kB]
2024-01-03T02:30:11.6666715Z #17 2.344 Get:32 http://deb.debian.org/debian bookworm/main amd64 libmpfr6 amd64 4.2.0-1 [701 kB]
2024-01-03T02:30:11.6667760Z #17 2.348 Get:33 http://deb.debian.org/debian bookworm/main amd64 libmpc3 amd64 1.3.1-1 [51.5 kB]
2024-01-03T02:30:11.6668746Z #17 2.348 Get:34 http://deb.debian.org/debian bookworm/main amd64 cpp-12 amd64 12.2.0-14 [9764 kB]
2024-01-03T02:30:11.6669815Z #17 2.389 Get:35 http://deb.debian.org/debian bookworm/main amd64 cpp amd64 4:12.2.0-3 [6836 B]
2024-01-03T02:30:11.6672391Z #17 2.389 Get:36 http://deb.debian.org/debian bookworm/main amd64 dumb-init amd64 1.2.5-2 [14.1 kB]
2024-01-03T02:30:11.6673639Z #17 2.389 Get:37 http://deb.debian.org/debian bookworm/main amd64 libcc1-0 amd64 12.2.0-14 [41.7 kB]
2024-01-03T02:30:11.6675955Z #17 2.390 Get:38 http://deb.debian.org/debian bookworm/main amd64 libgomp1 amd64 12.2.0-14 [116 kB]
2024-01-03T02:30:11.6677600Z #17 2.391 Get:39 http://deb.debian.org/debian bookworm/main amd64 libitm1 amd64 12.2.0-14 [26.1 kB]
2024-01-03T02:30:11.6680525Z #17 2.391 Get:40 http://deb.debian.org/debian bookworm/main amd64 libatomic1 amd64 12.2.0-14 [9328 B]
2024-01-03T02:30:11.6681537Z #17 2.391 Get:41 http://deb.debian.org/debian bookworm/main amd64 libasan8 amd64 12.2.0-14 [2195 kB]
2024-01-03T02:30:11.6683679Z #17 2.400 Get:42 http://deb.debian.org/debian bookworm/main amd64 liblsan0 amd64 12.2.0-14 [969 kB]
2024-01-03T02:30:11.6684769Z #17 2.404 Get:43 http://deb.debian.org/debian bookworm/main amd64 libtsan2 amd64 12.2.0-14 [2196 kB]
2024-01-03T02:30:11.6685774Z #17 2.413 Get:44 http://deb.debian.org/debian bookworm/main amd64 libubsan1 amd64 12.2.0-14 [883 kB]
2024-01-03T02:30:11.6688269Z #17 2.417 Get:45 http://deb.debian.org/debian bookworm/main amd64 libquadmath0 amd64 12.2.0-14 [144 kB]
2024-01-03T02:30:11.6689597Z #17 2.418 Get:46 http://deb.debian.org/debian bookworm/main amd64 libgcc-12-dev amd64 12.2.0-14 [2437 kB]
2024-01-03T02:30:11.6690628Z #17 2.431 Get:47 http://deb.debian.org/debian bookworm/main amd64 gcc-12 amd64 12.2.0-14 [19.3 MB]
2024-01-03T02:30:12.2325718Z #17 2.905 Get:48 http://deb.debian.org/debian bookworm/main amd64 gcc amd64 4:12.2.0-3 [5216 B]
2024-01-03T02:30:12.2328406Z #17 2.905 Get:49 http://deb.debian.org/debian bookworm/main amd64 libc-dev-bin amd64 2.36-9+deb12u3 [45.2 kB]
2024-01-03T02:30:12.2331886Z #17 2.905 Get:50 http://deb.debian.org/debian-security bookworm-security/main amd64 linux-libc-dev amd64 6.1.69-1 [1910 kB]
2024-01-03T02:30:12.2333874Z #17 2.909 Get:51 http://deb.debian.org/debian bookworm/main amd64 libcrypt-dev amd64 1:4.4.33-2 [118 kB]
2024-01-03T02:30:12.2335993Z #17 2.910 Get:52 http://deb.debian.org/debian bookworm/main amd64 libtirpc-dev amd64 1.3.3+ds-1 [191 kB]
2024-01-03T02:30:12.2337335Z #17 2.911 Get:53 http://deb.debian.org/debian bookworm/main amd64 libnsl-dev amd64 1.3.0-2 [66.4 kB]
2024-01-03T02:30:12.2338818Z #17 2.912 Get:54 http://deb.debian.org/debian bookworm/main amd64 rpcsvc-proto amd64 1.4.3-1 [63.3 kB]
2024-01-03T02:30:12.2340789Z #17 2.912 Get:55 http://deb.debian.org/debian bookworm/main amd64 libc6-dev amd64 2.36-9+deb12u3 [1898 kB]
2024-01-03T02:30:12.2342040Z #17 2.924 Get:56 http://deb.debian.org/debian bookworm/main amd64 libstdc++-12-dev amd64 12.2.0-14 [2046 kB]
2024-01-03T02:30:12.2343618Z #17 2.935 Get:57 http://deb.debian.org/debian bookworm/main amd64 g++-12 amd64 12.2.0-14 [10.7 MB]
2024-01-03T02:30:12.2344885Z #17 2.997 Get:58 http://deb.debian.org/debian bookworm/main amd64 g++ amd64 4:12.2.0-3 [1356 B]
2024-01-03T02:30:12.3423891Z #17 2.998 Get:59 http://deb.debian.org/debian bookworm/main amd64 libnl-3-200 amd64 3.7.0-0.2+b1 [63.1 kB]
2024-01-03T02:30:12.3426595Z #17 2.998 Get:60 http://deb.debian.org/debian bookworm/main amd64 libnl-genl-3-200 amd64 3.7.0-0.2+b1 [21.6 kB]
2024-01-03T02:30:12.3428162Z #17 2.999 Get:61 http://deb.debian.org/debian bookworm/main amd64 htop amd64 3.2.2-2 [152 kB]
2024-01-03T02:30:12.3429248Z #17 2.999 Get:62 http://deb.debian.org/debian bookworm/main amd64 make amd64 4.3-4.1 [396 kB]
2024-01-03T02:30:12.3430174Z #17 3.090 debconf: delaying package configuration, since apt-utils is not installed
2024-01-03T02:30:12.3430848Z #17 3.107 Fetched 73.0 MB in 1s (84.8 MB/s)
2024-01-03T02:30:12.4880681Z #17 3.122 Selecting previously unselected package libssl3:amd64.
2024-01-03T02:30:12.4881818Z #17 3.122 (Reading database ... 
2024-01-03T02:30:12.4882512Z (Reading database ... 5%
2024-01-03T02:30:12.4883148Z (Reading database ... 10%
2024-01-03T02:30:12.4883920Z (Reading database ... 15%
2024-01-03T02:30:12.4884591Z (Reading database ... 20%
2024-01-03T02:30:12.4885077Z (Reading database ... 25%
2024-01-03T02:30:12.4885477Z (Reading database ... 30%
2024-01-03T02:30:12.4885845Z (Reading database ... 35%
2024-01-03T02:30:12.4886274Z (Reading database ... 40%
2024-01-03T02:30:12.4886672Z (Reading database ... 45%
2024-01-03T02:30:12.4887069Z (Reading database ... 50%
2024-01-03T02:30:12.4887791Z (Reading database ... 55%
2024-01-03T02:30:12.4888461Z (Reading database ... 60%
2024-01-03T02:30:12.4889287Z (Reading database ... 65%
2024-01-03T02:30:12.4890019Z (Reading database ... 70%
2024-01-03T02:30:12.4890689Z (Reading database ... 75%
2024-01-03T02:30:12.4891260Z (Reading database ... 80%
2024-01-03T02:30:12.4891693Z (Reading database ... 85%
2024-01-03T02:30:12.4892197Z (Reading database ... 90%
2024-01-03T02:30:12.4892673Z (Reading database ... 95%
2024-01-03T02:30:12.4893136Z (Reading database ... 100%
2024-01-03T02:30:12.4893827Z (Reading database ... 6098 files and directories currently installed.)
2024-01-03T02:30:12.4895201Z #17 3.127 Preparing to unpack .../libssl3_3.0.11-1~deb12u2_amd64.deb ...
2024-01-03T02:30:12.4895914Z #17 3.130 Unpacking libssl3:amd64 (3.0.11-1~deb12u2) ...
2024-01-03T02:30:12.4896968Z #17 3.253 Selecting previously unselected package libpython3.11-minimal:amd64.
2024-01-03T02:30:12.6033057Z #17 3.254 Preparing to unpack .../libpython3.11-minimal_3.11.2-6_amd64.deb ...
2024-01-03T02:30:12.6034012Z #17 3.255 Unpacking libpython3.11-minimal:amd64 (3.11.2-6) ...
2024-01-03T02:30:12.6034866Z #17 3.342 Selecting previously unselected package libexpat1:amd64.
2024-01-03T02:30:12.6035602Z #17 3.343 Preparing to unpack .../libexpat1_2.5.0-1_amd64.deb ...
2024-01-03T02:30:12.6036307Z #17 3.345 Unpacking libexpat1:amd64 (2.5.0-1) ...
2024-01-03T02:30:12.6036997Z #17 3.368 Selecting previously unselected package python3.11-minimal.
2024-01-03T02:30:12.7442945Z #17 3.369 Preparing to unpack .../python3.11-minimal_3.11.2-6_amd64.deb ...
2024-01-03T02:30:12.7444203Z #17 3.373 Unpacking python3.11-minimal (3.11.2-6) ...
2024-01-03T02:30:12.7445277Z #17 3.509 Setting up libssl3:amd64 (3.0.11-1~deb12u2) ...
2024-01-03T02:30:12.8953089Z #17 3.512 Setting up libpython3.11-minimal:amd64 (3.11.2-6) ...
2024-01-03T02:30:12.8954539Z #17 3.517 Setting up libexpat1:amd64 (2.5.0-1) ...
2024-01-03T02:30:12.8955631Z #17 3.520 Setting up python3.11-minimal (3.11.2-6) ...
2024-01-03T02:30:13.3160143Z #17 4.054 Selecting previously unselected package python3-minimal.
2024-01-03T02:30:13.3160920Z #17 4.054 (Reading database ... 
2024-01-03T02:30:13.3161340Z (Reading database ... 5%
2024-01-03T02:30:13.3161855Z (Reading database ... 10%
2024-01-03T02:30:13.3162284Z (Reading database ... 15%
2024-01-03T02:30:13.3162734Z (Reading database ... 20%
2024-01-03T02:30:13.3163100Z (Reading database ... 25%
2024-01-03T02:30:13.3163778Z (Reading database ... 30%
2024-01-03T02:30:13.3164617Z (Reading database ... 35%
2024-01-03T02:30:13.3165344Z (Reading database ... 40%
2024-01-03T02:30:13.3166094Z (Reading database ... 45%
2024-01-03T02:30:13.3166929Z (Reading database ... 50%
2024-01-03T02:30:13.3167392Z (Reading database ... 55%
2024-01-03T02:30:13.3167852Z (Reading database ... 60%
2024-01-03T02:30:13.3168379Z (Reading database ... 65%
2024-01-03T02:30:13.3168753Z (Reading database ... 70%
2024-01-03T02:30:13.3169297Z (Reading database ... 75%
2024-01-03T02:30:13.3169676Z (Reading database ... 80%
2024-01-03T02:30:13.3170100Z (Reading database ... 85%
2024-01-03T02:30:13.3170637Z (Reading database ... 90%
2024-01-03T02:30:13.3171013Z (Reading database ... 95%
2024-01-03T02:30:13.3171465Z (Reading database ... 100%
2024-01-03T02:30:13.3172112Z (Reading database ... 6426 files and directories currently installed.)
2024-01-03T02:30:13.3172975Z #17 4.059 Preparing to unpack .../00-python3-minimal_3.11.2-1+b1_amd64.deb ...
2024-01-03T02:30:13.3173793Z #17 4.061 Unpacking python3-minimal (3.11.2-1+b1) ...
2024-01-03T02:30:13.3174642Z #17 4.081 Selecting previously unselected package media-types.
2024-01-03T02:30:13.4339189Z #17 4.082 Preparing to unpack .../01-media-types_10.0.0_all.deb ...
2024-01-03T02:30:13.4340095Z #17 4.083 Unpacking media-types (10.0.0) ...
2024-01-03T02:30:13.4340971Z #17 4.105 Selecting previously unselected package libncursesw6:amd64.
2024-01-03T02:30:13.4341907Z #17 4.106 Preparing to unpack .../02-libncursesw6_6.4-4_amd64.deb ...
2024-01-03T02:30:13.4342656Z #17 4.107 Unpacking libncursesw6:amd64 (6.4-4) ...
2024-01-03T02:30:13.4343511Z #17 4.132 Selecting previously unselected package libkrb5support0:amd64.
2024-01-03T02:30:13.4344877Z #17 4.133 Preparing to unpack .../03-libkrb5support0_1.20.1-2+deb12u1_amd64.deb ...
2024-01-03T02:30:13.4346424Z #17 4.134 Unpacking libkrb5support0:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:13.4347625Z #17 4.154 Selecting previously unselected package libk5crypto3:amd64.
2024-01-03T02:30:13.4348838Z #17 4.155 Preparing to unpack .../04-libk5crypto3_1.20.1-2+deb12u1_amd64.deb ...
2024-01-03T02:30:13.4349749Z #17 4.157 Unpacking libk5crypto3:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:13.4350403Z #17 4.178 Selecting previously unselected package libkeyutils1:amd64.
2024-01-03T02:30:13.4351224Z #17 4.179 Preparing to unpack .../05-libkeyutils1_1.6.3-2_amd64.deb ...
2024-01-03T02:30:13.4352393Z #17 4.180 Unpacking libkeyutils1:amd64 (1.6.3-2) ...
2024-01-03T02:30:13.4353748Z #17 4.199 Selecting previously unselected package libkrb5-3:amd64.
2024-01-03T02:30:13.5490057Z #17 4.200 Preparing to unpack .../06-libkrb5-3_1.20.1-2+deb12u1_amd64.deb ...
2024-01-03T02:30:13.5491252Z #17 4.201 Unpacking libkrb5-3:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:13.5492130Z #17 4.242 Selecting previously unselected package libgssapi-krb5-2:amd64.
2024-01-03T02:30:13.5492993Z #17 4.243 Preparing to unpack .../07-libgssapi-krb5-2_1.20.1-2+deb12u1_amd64.deb ...
2024-01-03T02:30:13.5493802Z #17 4.245 Unpacking libgssapi-krb5-2:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:13.5494991Z #17 4.267 Selecting previously unselected package libtirpc-common.
2024-01-03T02:30:13.5495996Z #17 4.268 Preparing to unpack .../08-libtirpc-common_1.3.3+ds-1_all.deb ...
2024-01-03T02:30:13.5497316Z #17 4.269 Unpacking libtirpc-common (1.3.3+ds-1) ...
2024-01-03T02:30:13.5498573Z #17 4.289 Selecting previously unselected package libtirpc3:amd64.
2024-01-03T02:30:13.5499869Z #17 4.289 Preparing to unpack .../09-libtirpc3_1.3.3+ds-1_amd64.deb ...
2024-01-03T02:30:13.5500695Z #17 4.291 Unpacking libtirpc3:amd64 (1.3.3+ds-1) ...
2024-01-03T02:30:13.5501319Z #17 4.314 Selecting previously unselected package libnsl2:amd64.
2024-01-03T02:30:13.6798719Z #17 4.315 Preparing to unpack .../10-libnsl2_1.3.0-2_amd64.deb ...
2024-01-03T02:30:13.6799510Z #17 4.317 Unpacking libnsl2:amd64 (1.3.0-2) ...
2024-01-03T02:30:13.6800276Z #17 4.335 Selecting previously unselected package readline-common.
2024-01-03T02:30:13.6801276Z #17 4.336 Preparing to unpack .../11-readline-common_8.2-1.3_all.deb ...
2024-01-03T02:30:13.6801957Z #17 4.337 Unpacking readline-common (8.2-1.3) ...
2024-01-03T02:30:13.6802665Z #17 4.359 Selecting previously unselected package libreadline8:amd64.
2024-01-03T02:30:13.6803611Z #17 4.359 Preparing to unpack .../12-libreadline8_8.2-1.3_amd64.deb ...
2024-01-03T02:30:13.6804974Z #17 4.361 Unpacking libreadline8:amd64 (8.2-1.3) ...
2024-01-03T02:30:13.6806324Z #17 4.387 Selecting previously unselected package libsqlite3-0:amd64.
2024-01-03T02:30:13.6807340Z #17 4.388 Preparing to unpack .../13-libsqlite3-0_3.40.1-2_amd64.deb ...
2024-01-03T02:30:13.6808163Z #17 4.389 Unpacking libsqlite3-0:amd64 (3.40.1-2) ...
2024-01-03T02:30:13.6808938Z #17 4.445 Selecting previously unselected package libpython3.11-stdlib:amd64.
2024-01-03T02:30:13.8095648Z #17 4.446 Preparing to unpack .../14-libpython3.11-stdlib_3.11.2-6_amd64.deb ...
2024-01-03T02:30:13.8097069Z #17 4.447 Unpacking libpython3.11-stdlib:amd64 (3.11.2-6) ...
2024-01-03T02:30:13.8098003Z #17 4.574 Selecting previously unselected package python3.11.
2024-01-03T02:30:13.9601991Z #17 4.576 Preparing to unpack .../15-python3.11_3.11.2-6_amd64.deb ...
2024-01-03T02:30:13.9603094Z #17 4.577 Unpacking python3.11 (3.11.2-6) ...
2024-01-03T02:30:13.9604134Z #17 4.600 Selecting previously unselected package libpython3-stdlib:amd64.
2024-01-03T02:30:13.9605043Z #17 4.601 Preparing to unpack .../16-libpython3-stdlib_3.11.2-1+b1_amd64.deb ...
2024-01-03T02:30:13.9605873Z #17 4.602 Unpacking libpython3-stdlib:amd64 (3.11.2-1+b1) ...
2024-01-03T02:30:13.9606516Z #17 4.619 Setting up python3-minimal (3.11.2-1+b1) ...
2024-01-03T02:30:14.1112016Z #17 4.732 Selecting previously unselected package python3.
2024-01-03T02:30:14.1113010Z #17 4.732 (Reading database ... 
2024-01-03T02:30:14.1113475Z (Reading database ... 5%
2024-01-03T02:30:14.1113974Z (Reading database ... 10%
2024-01-03T02:30:14.1114370Z (Reading database ... 15%
2024-01-03T02:30:14.1114770Z (Reading database ... 20%
2024-01-03T02:30:14.1115223Z (Reading database ... 25%
2024-01-03T02:30:14.1115614Z (Reading database ... 30%
2024-01-03T02:30:14.1116303Z (Reading database ... 35%
2024-01-03T02:30:14.1116823Z (Reading database ... 40%
2024-01-03T02:30:14.1117237Z (Reading database ... 45%
2024-01-03T02:30:14.1117672Z (Reading database ... 50%
2024-01-03T02:30:14.1118078Z (Reading database ... 55%
2024-01-03T02:30:14.1118470Z (Reading database ... 60%
2024-01-03T02:30:14.1118900Z (Reading database ... 65%
2024-01-03T02:30:14.1119684Z (Reading database ... 70%
2024-01-03T02:30:14.1120058Z (Reading database ... 75%
2024-01-03T02:30:14.1120500Z (Reading database ... 80%
2024-01-03T02:30:14.1120896Z (Reading database ... 85%
2024-01-03T02:30:14.1121330Z (Reading database ... 90%
2024-01-03T02:30:14.1121704Z (Reading database ... 95%
2024-01-03T02:30:14.1122069Z (Reading database ... 100%
2024-01-03T02:30:14.1122675Z (Reading database ... 6934 files and directories currently installed.)
2024-01-03T02:30:14.1123661Z #17 4.736 Preparing to unpack .../00-python3_3.11.2-1+b1_amd64.deb ...
2024-01-03T02:30:14.1124293Z #17 4.740 Unpacking python3 (3.11.2-1+b1) ...
2024-01-03T02:30:14.1125027Z #17 4.757 Selecting previously unselected package binutils-common:amd64.
2024-01-03T02:30:14.1125792Z #17 4.758 Preparing to unpack .../01-binutils-common_2.40-2_amd64.deb ...
2024-01-03T02:30:14.1126823Z #17 4.759 Unpacking binutils-common:amd64 (2.40-2) ...
2024-01-03T02:30:14.2349549Z #17 4.918 Selecting previously unselected package libbinutils:amd64.
2024-01-03T02:30:14.2351040Z #17 4.920 Preparing to unpack .../02-libbinutils_2.40-2_amd64.deb ...
2024-01-03T02:30:14.2351738Z #17 4.921 Unpacking libbinutils:amd64 (2.40-2) ...
2024-01-03T02:30:14.2352510Z #17 4.973 Selecting previously unselected package libctf-nobfd0:amd64.
2024-01-03T02:30:14.2353274Z #17 4.974 Preparing to unpack .../03-libctf-nobfd0_2.40-2_amd64.deb ...
2024-01-03T02:30:14.2353943Z #17 4.975 Unpacking libctf-nobfd0:amd64 (2.40-2) ...
2024-01-03T02:30:14.2354843Z #17 5.000 Selecting previously unselected package libctf0:amd64.
2024-01-03T02:30:14.3459384Z #17 5.001 Preparing to unpack .../04-libctf0_2.40-2_amd64.deb ...
2024-01-03T02:30:14.3460445Z #17 5.002 Unpacking libctf0:amd64 (2.40-2) ...
2024-01-03T02:30:14.3461563Z #17 5.022 Selecting previously unselected package libgprofng0:amd64.
2024-01-03T02:30:14.3462807Z #17 5.023 Preparing to unpack .../05-libgprofng0_2.40-2_amd64.deb ...
2024-01-03T02:30:14.3463949Z #17 5.024 Unpacking libgprofng0:amd64 (2.40-2) ...
2024-01-03T02:30:14.3464993Z #17 5.089 Selecting previously unselected package libjansson4:amd64.
2024-01-03T02:30:14.3466452Z #17 5.090 Preparing to unpack .../06-libjansson4_2.14-2_amd64.deb ...
2024-01-03T02:30:14.3467572Z #17 5.091 Unpacking libjansson4:amd64 (2.14-2) ...
2024-01-03T02:30:14.3468700Z #17 5.111 Selecting previously unselected package binutils-x86-64-linux-gnu.
2024-01-03T02:30:14.4959117Z #17 5.112 Preparing to unpack .../07-binutils-x86-64-linux-gnu_2.40-2_amd64.deb ...
2024-01-03T02:30:14.4960538Z #17 5.114 Unpacking binutils-x86-64-linux-gnu (2.40-2) ...
2024-01-03T02:30:14.5961634Z #17 5.277 Selecting previously unselected package binutils.
2024-01-03T02:30:14.5963024Z #17 5.278 Preparing to unpack .../08-binutils_2.40-2_amd64.deb ...
2024-01-03T02:30:14.5963813Z #17 5.279 Unpacking binutils (2.40-2) ...
2024-01-03T02:30:14.5964387Z #17 5.301 Selecting previously unselected package libisl23:amd64.
2024-01-03T02:30:14.5965084Z #17 5.302 Preparing to unpack .../09-libisl23_0.25-1_amd64.deb ...
2024-01-03T02:30:14.5965807Z #17 5.303 Unpacking libisl23:amd64 (0.25-1) ...
2024-01-03T02:30:14.5966451Z #17 5.360 Selecting previously unselected package libmpfr6:amd64.
2024-01-03T02:30:14.5967217Z #17 5.361 Preparing to unpack .../10-libmpfr6_4.2.0-1_amd64.deb ...
2024-01-03T02:30:14.7466950Z #17 5.363 Unpacking libmpfr6:amd64 (4.2.0-1) ...
2024-01-03T02:30:14.7468041Z #17 5.402 Selecting previously unselected package libmpc3:amd64.
2024-01-03T02:30:14.7469559Z #17 5.403 Preparing to unpack .../11-libmpc3_1.3.1-1_amd64.deb ...
2024-01-03T02:30:14.7470628Z #17 5.404 Unpacking libmpc3:amd64 (1.3.1-1) ...
2024-01-03T02:30:14.7471657Z #17 5.420 Selecting previously unselected package cpp-12.
2024-01-03T02:30:14.7472421Z #17 5.421 Preparing to unpack .../12-cpp-12_12.2.0-14_amd64.deb ...
2024-01-03T02:30:14.7473093Z #17 5.422 Unpacking cpp-12 (12.2.0-14) ...
2024-01-03T02:30:15.1687117Z #17 5.934 Selecting previously unselected package cpp.
2024-01-03T02:30:15.2757363Z #17 5.935 Preparing to unpack .../13-cpp_4%3a12.2.0-3_amd64.deb ...
2024-01-03T02:30:15.2758479Z #17 5.936 Unpacking cpp (4:12.2.0-3) ...
2024-01-03T02:30:15.2759104Z #17 5.951 Selecting previously unselected package dumb-init.
2024-01-03T02:30:15.2759893Z #17 5.952 Preparing to unpack .../14-dumb-init_1.2.5-2_amd64.deb ...
2024-01-03T02:30:15.2760524Z #17 5.953 Unpacking dumb-init (1.2.5-2) ...
2024-01-03T02:30:15.2761541Z #17 5.971 Selecting previously unselected package libcc1-0:amd64.
2024-01-03T02:30:15.2763083Z #17 5.972 Preparing to unpack .../15-libcc1-0_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.2764199Z #17 5.973 Unpacking libcc1-0:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.2764818Z #17 5.992 Selecting previously unselected package libgomp1:amd64.
2024-01-03T02:30:15.2765696Z #17 5.993 Preparing to unpack .../16-libgomp1_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.2766341Z #17 5.994 Unpacking libgomp1:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.2766993Z #17 6.020 Selecting previously unselected package libitm1:amd64.
2024-01-03T02:30:15.2767831Z #17 6.020 Preparing to unpack .../17-libitm1_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.2768463Z #17 6.022 Unpacking libitm1:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.2769135Z #17 6.041 Selecting previously unselected package libatomic1:amd64.
2024-01-03T02:30:15.4258489Z #17 6.041 Preparing to unpack .../18-libatomic1_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.4259716Z #17 6.043 Unpacking libatomic1:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.4260341Z #17 6.060 Selecting previously unselected package libasan8:amd64.
2024-01-03T02:30:15.4261442Z #17 6.060 Preparing to unpack .../19-libasan8_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.4262138Z #17 6.062 Unpacking libasan8:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.5261560Z #17 6.215 Selecting previously unselected package liblsan0:amd64.
2024-01-03T02:30:15.5262958Z #17 6.216 Preparing to unpack .../20-liblsan0_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.5264068Z #17 6.217 Unpacking liblsan0:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.5265067Z #17 6.290 Selecting previously unselected package libtsan2:amd64.
2024-01-03T02:30:15.5266022Z #17 6.291 Preparing to unpack .../21-libtsan2_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.6766225Z #17 6.292 Unpacking libtsan2:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.7769839Z #17 6.442 Selecting previously unselected package libubsan1:amd64.
2024-01-03T02:30:15.7771190Z #17 6.443 Preparing to unpack .../22-libubsan1_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.7772466Z #17 6.444 Unpacking libubsan1:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.7773496Z #17 6.514 Selecting previously unselected package libquadmath0:amd64.
2024-01-03T02:30:15.7774871Z #17 6.516 Preparing to unpack .../23-libquadmath0_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.7776014Z #17 6.517 Unpacking libquadmath0:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.7777317Z #17 6.541 Selecting previously unselected package libgcc-12-dev:amd64.
2024-01-03T02:30:15.7779505Z #17 6.542 Preparing to unpack .../24-libgcc-12-dev_12.2.0-14_amd64.deb ...
2024-01-03T02:30:15.9253940Z #17 6.543 Unpacking libgcc-12-dev:amd64 (12.2.0-14) ...
2024-01-03T02:30:15.9255146Z #17 6.690 Selecting previously unselected package gcc-12.
2024-01-03T02:30:16.0759745Z #17 6.691 Preparing to unpack .../25-gcc-12_12.2.0-14_amd64.deb ...
2024-01-03T02:30:16.0761136Z #17 6.692 Unpacking gcc-12 (12.2.0-14) ...
2024-01-03T02:30:16.6333073Z #17 7.362 Selecting previously unselected package gcc.
2024-01-03T02:30:16.6334221Z #17 7.363 Preparing to unpack .../26-gcc_4%3a12.2.0-3_amd64.deb ...
2024-01-03T02:30:16.6335184Z #17 7.364 Unpacking gcc (4:12.2.0-3) ...
2024-01-03T02:30:16.6335813Z #17 7.380 Selecting previously unselected package libc-dev-bin.
2024-01-03T02:30:16.6336702Z #17 7.381 Preparing to unpack .../27-libc-dev-bin_2.36-9+deb12u3_amd64.deb ...
2024-01-03T02:30:16.6337398Z #17 7.382 Unpacking libc-dev-bin (2.36-9+deb12u3) ...
2024-01-03T02:30:16.6338224Z #17 7.398 Selecting previously unselected package linux-libc-dev:amd64.
2024-01-03T02:30:16.7837385Z #17 7.399 Preparing to unpack .../28-linux-libc-dev_6.1.69-1_amd64.deb ...
2024-01-03T02:30:16.7838704Z #17 7.400 Unpacking linux-libc-dev:amd64 (6.1.69-1) ...
2024-01-03T02:30:16.9017319Z #17 7.585 Selecting previously unselected package libcrypt-dev:amd64.
2024-01-03T02:30:16.9018371Z #17 7.586 Preparing to unpack .../29-libcrypt-dev_1%3a4.4.33-2_amd64.deb ...
2024-01-03T02:30:16.9019099Z #17 7.592 Unpacking libcrypt-dev:amd64 (1:4.4.33-2) ...
2024-01-03T02:30:16.9019842Z #17 7.613 Selecting previously unselected package libtirpc-dev:amd64.
2024-01-03T02:30:16.9020634Z #17 7.615 Preparing to unpack .../30-libtirpc-dev_1.3.3+ds-1_amd64.deb ...
2024-01-03T02:30:16.9021320Z #17 7.616 Unpacking libtirpc-dev:amd64 (1.3.3+ds-1) ...
2024-01-03T02:30:16.9022074Z #17 7.645 Selecting previously unselected package libnsl-dev:amd64.
2024-01-03T02:30:16.9022792Z #17 7.646 Preparing to unpack .../31-libnsl-dev_1.3.0-2_amd64.deb ...
2024-01-03T02:30:16.9023416Z #17 7.647 Unpacking libnsl-dev:amd64 (1.3.0-2) ...
2024-01-03T02:30:16.9024137Z #17 7.667 Selecting previously unselected package rpcsvc-proto.
2024-01-03T02:30:17.0522749Z #17 7.668 Preparing to unpack .../32-rpcsvc-proto_1.4.3-1_amd64.deb ...
2024-01-03T02:30:17.0523664Z #17 7.669 Unpacking rpcsvc-proto (1.4.3-1) ...
2024-01-03T02:30:17.0524408Z #17 7.693 Selecting previously unselected package libc6-dev:amd64.
2024-01-03T02:30:17.0525190Z #17 7.694 Preparing to unpack .../33-libc6-dev_2.36-9+deb12u3_amd64.deb ...
2024-01-03T02:30:17.0526005Z #17 7.695 Unpacking libc6-dev:amd64 (2.36-9+deb12u3) ...
2024-01-03T02:30:17.2027749Z #17 7.840 Selecting previously unselected package libstdc++-12-dev:amd64.
2024-01-03T02:30:17.2028721Z #17 7.841 Preparing to unpack .../34-libstdc++-12-dev_12.2.0-14_amd64.deb ...
2024-01-03T02:30:17.2029460Z #17 7.842 Unpacking libstdc++-12-dev:amd64 (12.2.0-14) ...
2024-01-03T02:30:17.3537532Z #17 8.045 Selecting previously unselected package g++-12.
2024-01-03T02:30:17.3538772Z #17 8.047 Preparing to unpack .../35-g++-12_12.2.0-14_amd64.deb ...
2024-01-03T02:30:17.3539843Z #17 8.048 Unpacking g++-12 (12.2.0-14) ...
2024-01-03T02:30:17.7871306Z #17 8.552 Selecting previously unselected package g++.
2024-01-03T02:30:17.9200598Z #17 8.553 Preparing to unpack .../36-g++_4%3a12.2.0-3_amd64.deb ...
2024-01-03T02:30:17.9201741Z #17 8.555 Unpacking g++ (4:12.2.0-3) ...
2024-01-03T02:30:17.9202724Z #17 8.570 Selecting previously unselected package libnl-3-200:amd64.
2024-01-03T02:30:17.9203529Z #17 8.572 Preparing to unpack .../37-libnl-3-200_3.7.0-0.2+b1_amd64.deb ...
2024-01-03T02:30:17.9204601Z #17 8.573 Unpacking libnl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-03T02:30:17.9205871Z #17 8.595 Selecting previously unselected package libnl-genl-3-200:amd64.
2024-01-03T02:30:17.9206959Z #17 8.596 Preparing to unpack .../38-libnl-genl-3-200_3.7.0-0.2+b1_amd64.deb ...
2024-01-03T02:30:17.9207754Z #17 8.597 Unpacking libnl-genl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-03T02:30:17.9208456Z #17 8.611 Selecting previously unselected package htop.
2024-01-03T02:30:17.9209108Z #17 8.612 Preparing to unpack .../39-htop_3.2.2-2_amd64.deb ...
2024-01-03T02:30:17.9209966Z #17 8.613 Unpacking htop (3.2.2-2) ...
2024-01-03T02:30:17.9210586Z #17 8.637 Selecting previously unselected package make.
2024-01-03T02:30:17.9211331Z #17 8.638 Preparing to unpack .../40-make_4.3-4.1_amd64.deb ...
2024-01-03T02:30:17.9211989Z #17 8.640 Unpacking make (4.3-4.1) ...
2024-01-03T02:30:17.9212568Z #17 8.685 Setting up media-types (10.0.0) ...
2024-01-03T02:30:18.0280217Z #17 8.691 Setting up dumb-init (1.2.5-2) ...
2024-01-03T02:30:18.0281063Z #17 8.695 Setting up libkeyutils1:amd64 (1.6.3-2) ...
2024-01-03T02:30:18.0281824Z #17 8.710 Setting up libtirpc-common (1.3.3+ds-1) ...
2024-01-03T02:30:18.0282619Z #17 8.714 Setting up libsqlite3-0:amd64 (3.40.1-2) ...
2024-01-03T02:30:18.0283363Z #17 8.717 Setting up binutils-common:amd64 (2.40-2) ...
2024-01-03T02:30:18.0284292Z #17 8.720 Setting up linux-libc-dev:amd64 (6.1.69-1) ...
2024-01-03T02:30:18.0285035Z #17 8.723 Setting up libctf-nobfd0:amd64 (2.40-2) ...
2024-01-03T02:30:18.0286068Z #17 8.726 Setting up libgomp1:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.0286872Z #17 8.731 Setting up libjansson4:amd64 (2.14-2) ...
2024-01-03T02:30:18.0287722Z #17 8.735 Setting up libkrb5support0:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:18.0288483Z #17 8.738 Setting up rpcsvc-proto (1.4.3-1) ...
2024-01-03T02:30:18.0289206Z #17 8.741 Setting up make (4.3-4.1) ...
2024-01-03T02:30:18.0289953Z #17 8.745 Setting up libmpfr6:amd64 (4.2.0-1) ...
2024-01-03T02:30:18.0290683Z #17 8.749 Setting up libquadmath0:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.0291319Z #17 8.753 Setting up libmpc3:amd64 (1.3.1-1) ...
2024-01-03T02:30:18.0291925Z #17 8.756 Setting up libatomic1:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.0292583Z #17 8.760 Setting up libncursesw6:amd64 (6.4-4) ...
2024-01-03T02:30:18.0293375Z #17 8.763 Setting up libk5crypto3:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:18.0294126Z #17 8.770 Setting up libubsan1:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.0295222Z #17 8.773 Setting up libcrypt-dev:amd64 (1:4.4.33-2) ...
2024-01-03T02:30:18.0295910Z #17 8.781 Setting up libasan8:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.0296744Z #17 8.784 Setting up libnl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-03T02:30:18.0297511Z #17 8.793 Setting up libkrb5-3:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:18.1300099Z #17 8.796 Setting up libtsan2:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.1301416Z #17 8.799 Setting up libbinutils:amd64 (2.40-2) ...
2024-01-03T02:30:18.1302366Z #17 8.803 Setting up libisl23:amd64 (0.25-1) ...
2024-01-03T02:30:18.1303793Z #17 8.810 Setting up libc-dev-bin (2.36-9+deb12u3) ...
2024-01-03T02:30:18.1304806Z #17 8.817 Setting up readline-common (8.2-1.3) ...
2024-01-03T02:30:18.1305548Z #17 8.822 Setting up libcc1-0:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.1306494Z #17 8.826 Setting up liblsan0:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.1307185Z #17 8.831 Setting up libitm1:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.1307929Z #17 8.834 Setting up libctf0:amd64 (2.40-2) ...
2024-01-03T02:30:18.1308923Z #17 8.837 Setting up cpp-12 (12.2.0-14) ...
2024-01-03T02:30:18.1309651Z #17 8.840 Setting up libreadline8:amd64 (8.2-1.3) ...
2024-01-03T02:30:18.1310686Z #17 8.844 Setting up libgprofng0:amd64 (2.40-2) ...
2024-01-03T02:30:18.1311436Z #17 8.848 Setting up libgcc-12-dev:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.1312276Z #17 8.851 Setting up libgssapi-krb5-2:amd64 (1.20.1-2+deb12u1) ...
2024-01-03T02:30:18.1313324Z #17 8.857 Setting up cpp (4:12.2.0-3) ...
2024-01-03T02:30:18.1314429Z #17 8.864 Setting up libnl-genl-3-200:amd64 (3.7.0-0.2+b1) ...
2024-01-03T02:30:18.1315437Z #17 8.868 Setting up binutils-x86-64-linux-gnu (2.40-2) ...
2024-01-03T02:30:18.1316330Z #17 8.871 Setting up libtirpc3:amd64 (1.3.3+ds-1) ...
2024-01-03T02:30:18.1316979Z #17 8.875 Setting up htop (3.2.2-2) ...
2024-01-03T02:30:18.1317993Z #17 8.879 Setting up binutils (2.40-2) ...
2024-01-03T02:30:18.1319092Z #17 8.882 Setting up libtirpc-dev:amd64 (1.3.3+ds-1) ...
2024-01-03T02:30:18.1319928Z #17 8.886 Setting up gcc-12 (12.2.0-14) ...
2024-01-03T02:30:18.1320601Z #17 8.891 Setting up libnsl2:amd64 (1.3.0-2) ...
2024-01-03T02:30:18.1321395Z #17 8.895 Setting up libpython3.11-stdlib:amd64 (3.11.2-6) ...
2024-01-03T02:30:18.2809708Z #17 8.899 Setting up gcc (4:12.2.0-3) ...
2024-01-03T02:30:18.2810503Z #17 8.908 Setting up libnsl-dev:amd64 (1.3.0-2) ...
2024-01-03T02:30:18.2811163Z #17 8.911 Setting up libc6-dev:amd64 (2.36-9+deb12u3) ...
2024-01-03T02:30:18.2811828Z #17 8.914 Setting up libpython3-stdlib:amd64 (3.11.2-1+b1) ...
2024-01-03T02:30:18.2812535Z #17 8.918 Setting up python3.11 (3.11.2-6) ...
2024-01-03T02:30:18.7085981Z #17 9.473 Setting up libstdc++-12-dev:amd64 (12.2.0-14) ...
2024-01-03T02:30:18.8592365Z #17 9.477 Setting up python3 (3.11.2-1+b1) ...
2024-01-03T02:30:18.8593013Z #17 9.553 Setting up g++-12 (12.2.0-14) ...
2024-01-03T02:30:18.8593536Z #17 9.557 Setting up g++ (4:12.2.0-3) ...
2024-01-03T02:30:18.8594534Z #17 9.562 update-alternatives: using /usr/bin/g++ to provide /usr/bin/c++ (c++) in auto mode
2024-01-03T02:30:18.8595750Z #17 9.564 Processing triggers for libc-bin (2.36-9+deb12u3) ...
2024-01-03T02:30:19.5761951Z #17 DONE 10.3s
2024-01-03T02:30:19.7266221Z 
2024-01-03T02:30:19.7267333Z #18 [stage-0  8/12] COPY package-lock.json .
2024-01-03T02:30:19.7267885Z #18 DONE 0.0s
2024-01-03T02:30:19.7268104Z 
2024-01-03T02:30:19.7268337Z #19 [stage-0  9/12] COPY package.json .
2024-01-03T02:30:19.7268841Z #19 DONE 0.0s
2024-01-03T02:30:19.7269046Z 
2024-01-03T02:30:19.7269373Z #20 [stage-0 10/12] RUN --mount=type=cache,target=/root/.cache npm ci
2024-01-03T02:30:31.5999917Z #20 11.91 
2024-01-03T02:30:31.6000782Z #20 11.91 added 965 packages, and audited 966 packages in 11s
2024-01-03T02:30:31.6001882Z #20 11.91 
2024-01-03T02:30:31.6002500Z #20 11.91 184 packages are looking for funding
2024-01-03T02:30:31.6003298Z #20 11.91   run `npm fund` for details
2024-01-03T02:30:31.6004118Z #20 11.91 
2024-01-03T02:30:31.6004634Z #20 11.91 found 0 vulnerabilities
2024-01-03T02:30:31.6005243Z #20 11.91 npm notice 
2024-01-03T02:30:31.6006346Z #20 11.91 npm notice New patch version of npm available! 10.2.3 -> 10.2.5
2024-01-03T02:30:31.6007420Z #20 11.91 npm notice Changelog: <https://github.com/npm/cli/releases/tag/v10.2.5>
2024-01-03T02:30:31.6008693Z #20 11.91 npm notice Run `npm install -g npm@10.2.5` to update!
2024-01-03T02:30:31.6009247Z #20 11.91 npm notice 
2024-01-03T02:30:32.3459114Z #20 DONE 12.6s
2024-01-03T02:30:32.3459507Z 
2024-01-03T02:30:32.3460024Z #21 [stage-0 11/12] COPY . .
2024-01-03T02:30:32.3460887Z #21 DONE 0.1s
2024-01-03T02:30:32.4960083Z 
2024-01-03T02:30:32.4961465Z #22 [stage-0 12/12] RUN npm run build
2024-01-03T02:30:32.9475080Z #22 0.475 
2024-01-03T02:30:32.9476077Z #22 0.475 > skellybot@0.0.1 build
2024-01-03T02:30:32.9477199Z #22 0.475 > nest build
2024-01-03T02:30:32.9478050Z #22 0.475 
2024-01-03T02:30:36.9682164Z #22 4.621 npm notice 
2024-01-03T02:30:37.1182630Z #22 4.621 npm notice New patch version of npm available! 10.2.3 -> 10.2.5
2024-01-03T02:30:37.1184378Z #22 4.622 npm notice Changelog: <https://github.com/npm/cli/releases/tag/v10.2.5>
2024-01-03T02:30:37.1185778Z #22 4.622 npm notice Run `npm install -g npm@10.2.5` to update!
2024-01-03T02:30:37.1186669Z #22 4.622 npm notice 
2024-01-03T02:30:37.2689489Z #22 DONE 4.8s
2024-01-03T02:30:37.2689927Z 
2024-01-03T02:30:37.2690212Z #23 exporting to image
2024-01-03T02:30:37.2691019Z #23 exporting layers
2024-01-03T02:30:43.3245715Z #23 exporting layers 6.2s done
2024-01-03T02:30:43.3247146Z #23 writing image sha256:fcad9b030154424a2b2ef4aaf843bea06bdaeebd1be0eb6e3fc2d1e086e697fc done
2024-01-03T02:30:43.3249902Z #23 naming to us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:676f2b55cf418a17d13170730d6e74fdec198dea done
2024-01-03T02:30:43.3251507Z #23 DONE 6.2s
2024-01-03T02:30:43.4431887Z #0 building with "default" instance using docker driver
2024-01-03T02:30:43.4432444Z 
2024-01-03T02:30:43.4432693Z #1 [internal] load build definition from Dockerfile
2024-01-03T02:30:43.5888020Z #1 transferring dockerfile: 1.03kB done
2024-01-03T02:30:43.5889153Z #1 DONE 0.0s
2024-01-03T02:30:43.5890060Z 
2024-01-03T02:30:43.5890333Z #2 [internal] load .dockerignore
2024-01-03T02:30:43.5890981Z #2 transferring context: 57B done
2024-01-03T02:30:43.5891551Z #2 DONE 0.0s
2024-01-03T02:30:43.5891850Z 
2024-01-03T02:30:43.5892091Z #3 resolve image config for docker.io/docker/dockerfile:1.2
2024-01-03T02:30:43.5892786Z #3 DONE 0.1s
2024-01-03T02:30:43.7390948Z 
2024-01-03T02:30:43.7395052Z #4 docker-image://docker.io/docker/dockerfile:1.2@sha256:e2a8561e419ab1ba6b2fe6cbdf49fd92b95912df1cf7d313c3e2230a333fdbcc
2024-01-03T02:30:43.7396004Z #4 CACHED
2024-01-03T02:30:43.7396179Z 
2024-01-03T02:30:43.7396415Z #5 [internal] load build definition from Dockerfile
2024-01-03T02:30:43.7396997Z #5 DONE 0.0s
2024-01-03T02:30:43.7397195Z 
2024-01-03T02:30:43.7397382Z #6 [internal] load .dockerignore
2024-01-03T02:30:43.7397781Z #6 DONE 0.0s
2024-01-03T02:30:43.7398062Z 
2024-01-03T02:30:43.7398395Z #7 [internal] load metadata for docker.io/library/node:20.10.0-slim
2024-01-03T02:30:43.8367683Z #7 DONE 0.1s
2024-01-03T02:30:43.8368583Z 
2024-01-03T02:30:43.8369818Z #8 [stage-0  1/12] FROM docker.io/library/node:20.10.0-slim@sha256:5c714c3e90f66a2cbfa266b90a4d7adcd63453cd730aa2d13cba84b260bea2e6
2024-01-03T02:30:43.8370983Z #8 DONE 0.0s
2024-01-03T02:30:43.8371240Z 
2024-01-03T02:30:43.8371392Z #9 [internal] load build context
2024-01-03T02:30:43.8372060Z #9 transferring context: 13.84kB 0.0s done
2024-01-03T02:30:43.8372533Z #9 DONE 0.0s
2024-01-03T02:30:43.8372741Z 
2024-01-03T02:30:43.8373521Z #10 [stage-0  6/12] RUN useradd -m appuser && chown -R appuser /workspace && chown -R appuser "/home/.npm"
2024-01-03T02:30:43.8374459Z #10 CACHED
2024-01-03T02:30:43.8374736Z 
2024-01-03T02:30:43.8375519Z #11 [stage-0  5/12] RUN mkdir /home/.npm
2024-01-03T02:30:43.8376346Z #11 CACHED
2024-01-03T02:30:43.8376540Z 
2024-01-03T02:30:43.8376798Z #12 [stage-0  9/12] COPY package.json .
2024-01-03T02:30:43.8377300Z #12 CACHED
2024-01-03T02:30:43.8377479Z 
2024-01-03T02:30:43.8378044Z #13 [stage-0  3/12] RUN rm -rf /etc/apt/apt.conf.d/docker-clean
2024-01-03T02:30:43.8378566Z #13 CACHED
2024-01-03T02:30:43.8378729Z 
2024-01-03T02:30:43.8379020Z #14 [stage-0  2/12] WORKDIR /workspace
2024-01-03T02:30:43.8379670Z #14 CACHED
2024-01-03T02:30:43.8379843Z 
2024-01-03T02:30:43.8380217Z #15 [stage-0 10/12] RUN --mount=type=cache,target=/root/.cache npm ci
2024-01-03T02:30:43.8381023Z #15 CACHED
2024-01-03T02:30:43.8381295Z 
2024-01-03T02:30:43.8381572Z #16 [stage-0  4/12] COPY ./bin/builds/ .
2024-01-03T02:30:43.8382161Z #16 CACHED
2024-01-03T02:30:43.8382643Z 
2024-01-03T02:30:43.8382882Z #17 [stage-0 11/12] COPY . .
2024-01-03T02:30:43.8383270Z #17 CACHED
2024-01-03T02:30:43.8383558Z 
2024-01-03T02:30:43.8383921Z #18 [stage-0  8/12] COPY package-lock.json .
2024-01-03T02:30:43.8384378Z #18 CACHED
2024-01-03T02:30:43.8384570Z 
2024-01-03T02:30:43.8385475Z #19 [stage-0  7/12] RUN --mount=type=cache,target=/var/cache/apt ./install_packages     dumb-init     htop     make     g++     python3
2024-01-03T02:30:43.8386368Z #19 CACHED
2024-01-03T02:30:43.8386671Z 
2024-01-03T02:30:43.8386977Z #20 [stage-0 12/12] RUN npm run build
2024-01-03T02:30:43.8387486Z #20 CACHED
2024-01-03T02:30:43.8387683Z 
2024-01-03T02:30:43.8387837Z #21 exporting to image
2024-01-03T02:30:43.8388319Z #21 exporting layers done
2024-01-03T02:30:43.8389051Z #21 writing image sha256:fcad9b030154424a2b2ef4aaf843bea06bdaeebd1be0eb6e3fc2d1e086e697fc done
2024-01-03T02:30:43.8390018Z #21 naming to us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot:latest done
2024-01-03T02:30:43.8390663Z #21 DONE 0.0s
2024-01-03T02:30:43.8560248Z The push refers to repository [us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot]
2024-01-03T02:30:43.9494529Z b3c7467259e9: Preparing
2024-01-03T02:30:43.9496059Z 12ab71e11763: Preparing
2024-01-03T02:30:43.9497578Z 313da2cc0709: Preparing
2024-01-03T02:30:43.9498277Z d840ddb0de9a: Preparing
2024-01-03T02:30:43.9498789Z 34253bbb8c56: Preparing
2024-01-03T02:30:43.9499326Z 6271da7e1db8: Preparing
2024-01-03T02:30:43.9499754Z 9670a0129a94: Preparing
2024-01-03T02:30:43.9500223Z 0328c4df6e44: Preparing
2024-01-03T02:30:43.9500617Z c8cfecd17c73: Preparing
2024-01-03T02:30:43.9501021Z 950f606bdab1: Preparing
2024-01-03T02:30:43.9501471Z 6a031daedbbe: Preparing
2024-01-03T02:30:43.9501872Z 54670042a040: Preparing
2024-01-03T02:30:43.9502249Z 0d1064329154: Preparing
2024-01-03T02:30:43.9502694Z e15f668bdea1: Preparing
2024-01-03T02:30:43.9503089Z 6a02db9fb904: Preparing
2024-01-03T02:30:43.9503549Z 7292cf786aa8: Preparing
2024-01-03T02:30:43.9503958Z 6a031daedbbe: Waiting
2024-01-03T02:30:43.9504334Z 54670042a040: Waiting
2024-01-03T02:30:43.9504761Z 0d1064329154: Waiting
2024-01-03T02:30:43.9505146Z 6271da7e1db8: Waiting
2024-01-03T02:30:43.9505514Z e15f668bdea1: Waiting
2024-01-03T02:30:43.9505958Z 0328c4df6e44: Waiting
2024-01-03T02:30:43.9506326Z 6a02db9fb904: Waiting
2024-01-03T02:30:43.9506772Z c8cfecd17c73: Waiting
2024-01-03T02:30:43.9507171Z 950f606bdab1: Waiting
2024-01-03T02:30:43.9507880Z 7292cf786aa8: Waiting
2024-01-03T02:30:45.0313896Z b3c7467259e9: Pushed
2024-01-03T02:30:45.1450946Z d840ddb0de9a: Pushed
2024-01-03T02:30:45.1989674Z 34253bbb8c56: Pushed
2024-01-03T02:30:45.7720953Z 12ab71e11763: Pushed
2024-01-03T02:30:46.1308044Z 0328c4df6e44: Pushed
2024-01-03T02:30:46.1814740Z 9670a0129a94: Pushed
2024-01-03T02:30:46.7934038Z c8cfecd17c73: Pushed
2024-01-03T02:30:47.0204569Z 950f606bdab1: Pushed
2024-01-03T02:30:47.0251144Z 54670042a040: Layer already exists
2024-01-03T02:30:47.1681270Z 6a031daedbbe: Pushed
2024-01-03T02:30:47.2268368Z 0d1064329154: Layer already exists
2024-01-03T02:30:47.2527835Z e15f668bdea1: Layer already exists
2024-01-03T02:30:47.3745251Z 6a02db9fb904: Layer already exists
2024-01-03T02:30:47.4337072Z 7292cf786aa8: Layer already exists
2024-01-03T02:30:56.8346275Z 313da2cc0709: Pushed
2024-01-03T02:30:57.9080286Z 6271da7e1db8: Pushed
2024-01-03T02:30:59.2323388Z 676f2b55cf418a17d13170730d6e74fdec198dea: digest: sha256:7cf5b50013cbf99a0d6d0029452297a06ad259fd23a26abf9b9153ebf71a391c size: 3666
2024-01-03T02:30:59.2482346Z The push refers to repository [us-east1-docker.pkg.dev/mocap-test-project/jonbot/nestbot]
2024-01-03T02:30:59.4425353Z b3c7467259e9: Preparing
2024-01-03T02:30:59.4426403Z 12ab71e11763: Preparing
2024-01-03T02:30:59.4429974Z 313da2cc0709: Preparing
2024-01-03T02:30:59.4430735Z d840ddb0de9a: Preparing
2024-01-03T02:30:59.4431774Z 34253bbb8c56: Preparing
2024-01-03T02:30:59.4433694Z 6271da7e1db8: Preparing
2024-01-03T02:30:59.4434610Z 9670a0129a94: Preparing
2024-01-03T02:30:59.4435547Z 0328c4df6e44: Preparing
2024-01-03T02:30:59.4436074Z 6271da7e1db8: Waiting
2024-01-03T02:30:59.4436433Z 9670a0129a94: Waiting
2024-01-03T02:30:59.4436853Z c8cfecd17c73: Preparing
2024-01-03T02:30:59.4437232Z 0328c4df6e44: Waiting
2024-01-03T02:30:59.4437582Z 950f606bdab1: Preparing
2024-01-03T02:30:59.4438026Z 6a031daedbbe: Preparing
2024-01-03T02:30:59.4438446Z 950f606bdab1: Waiting
2024-01-03T02:30:59.4438801Z c8cfecd17c73: Waiting
2024-01-03T02:30:59.4439240Z 54670042a040: Preparing
2024-01-03T02:30:59.4439596Z 0d1064329154: Preparing
2024-01-03T02:30:59.4440028Z e15f668bdea1: Preparing
2024-01-03T02:30:59.4440390Z 6a031daedbbe: Waiting
2024-01-03T02:30:59.4440738Z 54670042a040: Waiting
2024-01-03T02:30:59.4441147Z 0d1064329154: Waiting
2024-01-03T02:30:59.4441484Z e15f668bdea1: Waiting
2024-01-03T02:30:59.4441848Z 6a02db9fb904: Preparing
2024-01-03T02:30:59.4442279Z 7292cf786aa8: Preparing
2024-01-03T02:30:59.4442697Z 6a02db9fb904: Waiting
2024-01-03T02:30:59.4443122Z 7292cf786aa8: Waiting
2024-01-03T02:30:59.6509965Z 34253bbb8c56: Layer already exists
2024-01-03T02:30:59.6562794Z 12ab71e11763: Layer already exists
2024-01-03T02:30:59.6592060Z 313da2cc0709: Layer already exists
2024-01-03T02:30:59.6656912Z d840ddb0de9a: Layer already exists
2024-01-03T02:30:59.6673084Z b3c7467259e9: Layer already exists
2024-01-03T02:30:59.7563627Z 6271da7e1db8: Layer already exists
2024-01-03T02:30:59.7667718Z 9670a0129a94: Layer already exists
2024-01-03T02:30:59.7704560Z 950f606bdab1: Layer already exists
2024-01-03T02:30:59.7838503Z c8cfecd17c73: Layer already exists
2024-01-03T02:30:59.8605798Z 0328c4df6e44: Layer already exists
2024-01-03T02:30:59.8692309Z 6a031daedbbe: Layer already exists
2024-01-03T02:30:59.8736243Z 54670042a040: Layer already exists
2024-01-03T02:30:59.8806532Z 0d1064329154: Layer already exists
2024-01-03T02:30:59.8900470Z e15f668bdea1: Layer already exists
2024-01-03T02:30:59.9711499Z 7292cf786aa8: Layer already exists
2024-01-03T02:31:00.0690343Z 6a02db9fb904: Layer already exists
2024-01-03T02:31:00.4210699Z latest: digest: sha256:7cf5b50013cbf99a0d6d0029452297a06ad259fd23a26abf9b9153ebf71a391c size: 3666
2024-01-03T02:31:00.4265744Z ##[group]Run gcloud compute instances stop skelly-bot-testing --zone=us-central1-a
2024-01-03T02:31:00.4266773Z [36;1mgcloud compute instances stop skelly-bot-testing --zone=us-central1-a[0m
2024-01-03T02:31:00.4267567Z [36;1mgcloud compute instances start skelly-bot-testing --zone=us-central1-a[0m
2024-01-03T02:31:00.4317697Z shell: /usr/bin/bash -e {0}
2024-01-03T02:31:00.4318199Z env:
2024-01-03T02:31:00.4318537Z   PROJECT_ID: mocap-test-project
2024-01-03T02:31:00.4318976Z   GAR_LOCATION: us-east1
2024-01-03T02:31:00.4319418Z   SERVICE: jonbot/nestbot
2024-01-03T02:31:00.4319808Z   REGION: us-central1
2024-01-03T02:31:00.4320560Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:00.4321588Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:00.4322715Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:00.4323437Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-03T02:31:00.4323907Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-03T02:31:00.4324397Z   GCLOUD_PROJECT: mocap-test-project
2024-01-03T02:31:00.4324851Z   GCP_PROJECT: mocap-test-project
2024-01-03T02:31:00.4325289Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-03T02:31:00.4325830Z ##[endgroup]
2024-01-03T02:31:03.6585667Z Stopping instance(s) skelly-bot-testing...
2024-01-03T02:31:44.6515602Z ............................................................................................................................................................................................................done.
2024-01-03T02:31:44.9291442Z Updated [https://compute.googleapis.com/compute/v1/projects/mocap-test-project/zones/us-central1-a/instances/skelly-bot-testing].
2024-01-03T02:31:46.8311906Z Starting instance(s) skelly-bot-testing...
2024-01-03T02:31:54.6366630Z ......................................done.
2024-01-03T02:31:54.8501558Z Updated [https://compute.googleapis.com/compute/v1/projects/mocap-test-project/zones/us-central1-a/instances/skelly-bot-testing].
2024-01-03T02:31:54.8502636Z Instance internal IP is 10.128.0.10
2024-01-03T02:31:54.8503152Z Instance external IP is 34.121.144.57
2024-01-03T02:31:54.9884792Z ##[group]Run echo 
2024-01-03T02:31:54.9885213Z [36;1mecho [0m
2024-01-03T02:31:54.9934739Z shell: /usr/bin/bash -e {0}
2024-01-03T02:31:54.9935230Z env:
2024-01-03T02:31:54.9935582Z   PROJECT_ID: mocap-test-project
2024-01-03T02:31:54.9936064Z   GAR_LOCATION: us-east1
2024-01-03T02:31:54.9936437Z   SERVICE: jonbot/nestbot
2024-01-03T02:31:54.9936821Z   REGION: us-central1
2024-01-03T02:31:54.9937567Z   CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:54.9938627Z   GOOGLE_APPLICATION_CREDENTIALS: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:54.9939574Z   GOOGLE_GHA_CREDS_PATH: /home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json
2024-01-03T02:31:54.9940332Z   CLOUDSDK_CORE_PROJECT: mocap-test-project
2024-01-03T02:31:54.9940824Z   CLOUDSDK_PROJECT: mocap-test-project
2024-01-03T02:31:54.9941327Z   GCLOUD_PROJECT: mocap-test-project
2024-01-03T02:31:54.9941872Z   GCP_PROJECT: mocap-test-project
2024-01-03T02:31:54.9942371Z   GOOGLE_CLOUD_PROJECT: mocap-test-project
2024-01-03T02:31:54.9942818Z ##[endgroup]
2024-01-03T02:31:55.0011357Z 
2024-01-03T02:31:55.0060976Z Post job cleanup.
2024-01-03T02:31:55.1085031Z [command]/usr/bin/docker logout us-east1-docker.pkg.dev
2024-01-03T02:31:55.1214109Z Removing login credentials for us-east1-docker.pkg.dev
2024-01-03T02:31:55.1364579Z Post job cleanup.
2024-01-03T02:31:55.2173201Z Removed exported credentials at "/home/runner/work/skellybot/skellybot/gha-creds-4199cb2c73bcb4f5.json".
2024-01-03T02:31:55.2351423Z Post job cleanup.
2024-01-03T02:31:55.3073758Z [command]/usr/bin/git version
2024-01-03T02:31:55.3112919Z git version 2.43.0
2024-01-03T02:31:55.3152984Z Temporarily overriding HOME='/home/runner/work/_temp/89f7f647-03ee-4d9e-ae84-652bbade38be' before making global git config changes
2024-01-03T02:31:55.3154758Z Adding repository directory to the temporary git global config as a safe directory
2024-01-03T02:31:55.3157716Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/skellybot/skellybot
2024-01-03T02:31:55.3190684Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2024-01-03T02:31:55.3222848Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2024-01-03T02:31:55.3464574Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2024-01-03T02:31:55.3484548Z http.https://github.com/.extraheader
2024-01-03T02:31:55.3495448Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2024-01-03T02:31:55.3526290Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2024-01-03T02:31:55.3993020Z Cleaning up orphan processes

LOGS FROM A WORKING DEPLOYMENT 
