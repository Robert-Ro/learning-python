
FROM jjanzic/docker-python3-opencv

ADD src/cv.py .
ENTRYPOINT python
CMD ["python", "cv.py"]