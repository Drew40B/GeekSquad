# Sample multi stage node js dockerfile

Based upon <https://www.feval.ca/posts/multistage-docker/>

## Stages

1. build and unit test
2. build in production mode
3. use smaller (slim) image for final result.

## Commands

- Build: `docker build . -t multistage-demo`
- Run Container: `docker run -itd --rm  -p 8000:8000 --name multi-demo multistage-demo`
- View Container logs: `docker logs --follow multi-demo`

## Notes

- Drew modified original 2 stages to 3 stages
