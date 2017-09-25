gyp capnproto.gyp -DOS=win -Dtarget_arch=x64 --depth=. -f msvs -G msvs_version=2017 -Dbuildtype=Debug --no-duplicate-basename-check --generator-output=./build.vs2017/

rem msbuild.exe ......SolutionFile.sln /t:Build/p:Configuration=Release;Platform=Win32