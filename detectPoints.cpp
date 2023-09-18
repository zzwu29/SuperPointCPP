#include <torch/script.h>
#include <iostream>
#include <memory>
#include <opencv2/opencv.hpp>

#include "NetWork.h"
#include "PointTracker.h"
#include "SuperPointFrontend.h"

#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/types_c.h>

#include <io.h>

void getFiles(std::string path, std::vector<std::string>& files)
{
    intptr_t   hFile = 0;
    struct _finddata_t fileinfo;
    std::string p;
    if ((hFile = _findfirst(p.assign(path).append("/*").c_str(), &fileinfo)) != -1)
    {
        do
        {
            if (strcmp(fileinfo.name, ".") != 0 && strcmp(fileinfo.name, "..") != 0)
            {
                files.push_back(p.assign(path).append("/").append(fileinfo.name));
            }
        } while (_findnext(hFile, &fileinfo) == 0);
        _findclose(hFile);
    }
}

int main(int argc, const char *argv[])
{
    std::string img_path("../assets/icl_snippet");
    std::string weight_path("../model/superpoint_v3_t.pt");


    std::vector<std::string> listening;
    getFiles(img_path, listening);

    for (auto it = listening.begin(); it != listening.end(); it++) {
        std::string img = *it;
        //std::cout << "img: " << img << std::endl;
        cv::Mat gray_img;
        SingleImage simg(img);
        gray_img = simg.readImage();
        // Superpoint Frontend to extract feature point
        SPFrontend spfrontend(weight_path, 4, 0.015, 0.7);
        std::vector<cv::KeyPoint> pts;
        cv::Mat descMat_out;
        spfrontend.run(gray_img, pts, descMat_out);
        // plot
        simg.draw(pts);
    }
    
    return 0;
}