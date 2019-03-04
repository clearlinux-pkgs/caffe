#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : caffe
Version  : 7d92d5c23d503af0565159b40c2d5155b5fdc3fb
Release  : 31
URL      : https://github.com/fenrus75/caffe/archive/7d92d5c23d503af0565159b40c2d5155b5fdc3fb.tar.gz
Source0  : https://github.com/fenrus75/caffe/archive/7d92d5c23d503af0565159b40c2d5155b5fdc3fb.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: caffe-bin = %{version}-%{release}
Requires: caffe-data = %{version}-%{release}
Requires: caffe-lib = %{version}-%{release}
Requires: caffe-license = %{version}-%{release}
Requires: caffe-python = %{version}-%{release}
Requires: Cython
Requires: Pillow
Requires: PyYAML
Requires: h5py
Requires: ipython
Requires: leveldb
Requires: matplotlib
Requires: networkx
Requires: nose
Requires: numpy
Requires: pandas
Requires: protobuf
Requires: python-dateutil
Requires: python-gflags
Requires: scikit-image
Requires: scipy
Requires: six
Requires: tornado
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : doxygen
BuildRequires : gflags-dev
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : glog-dev
BuildRequires : h5py
BuildRequires : hdf5-dev
BuildRequires : leveldb-dev
BuildRequires : lmdb-dev
BuildRequires : nose
BuildRequires : numpy
BuildRequires : numpy-legacypython
BuildRequires : openblas
BuildRequires : opencv-dev
BuildRequires : protobuf-dev
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : scipy
BuildRequires : snappy-dev
BuildRequires : zlib-dev
Patch1: config.patch
Patch2: py3.patch

%description
# Caffe
[![Build Status](https://travis-ci.org/BVLC/caffe.svg?branch=master)](https://travis-ci.org/BVLC/caffe)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](LICENSE)

%package bin
Summary: bin components for the caffe package.
Group: Binaries
Requires: caffe-data = %{version}-%{release}
Requires: caffe-license = %{version}-%{release}

%description bin
bin components for the caffe package.


%package data
Summary: data components for the caffe package.
Group: Data

%description data
data components for the caffe package.


%package dev
Summary: dev components for the caffe package.
Group: Development
Requires: caffe-lib = %{version}-%{release}
Requires: caffe-bin = %{version}-%{release}
Requires: caffe-data = %{version}-%{release}
Provides: caffe-devel = %{version}-%{release}

%description dev
dev components for the caffe package.


%package legacypython
Summary: legacypython components for the caffe package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the caffe package.


%package lib
Summary: lib components for the caffe package.
Group: Libraries
Requires: caffe-data = %{version}-%{release}
Requires: caffe-license = %{version}-%{release}

%description lib
lib components for the caffe package.


%package license
Summary: license components for the caffe package.
Group: Default

%description license
license components for the caffe package.


%package python
Summary: python components for the caffe package.
Group: Default

%description python
python components for the caffe package.


%prep
%setup -q -n caffe-7d92d5c23d503af0565159b40c2d5155b5fdc3fb
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551729511
mkdir -p clr-build
pushd clr-build
export LDFLAGS="${LDFLAGS} -fno-lto"
export CFLAGS="$CFLAGS -ffast-math -ftree-loop-vectorize "
export FCFLAGS="$CFLAGS -ffast-math -ftree-loop-vectorize "
export FFLAGS="$CFLAGS -ffast-math -ftree-loop-vectorize "
export CXXFLAGS="$CXXFLAGS -ffast-math -ftree-loop-vectorize "
%cmake .. -DUSE_LEVELDB=on -DUSE_OPENCV=off  -DBLAS=open -DBUILD_python=off
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1551729511
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/caffe
cp LICENSE %{buildroot}/usr/share/package-licenses/caffe/LICENSE
pushd clr-build
%make_install
popd
## install_append content
mkdir -p %{buildroot}/usr/lib64
mv %{buildroot}/usr/lib/lib*so* %{buildroot}/usr/lib64
mkdir -p %{buildroot}/usr/lib/python2.7/site-packages/
mv %{buildroot}/usr/python/* %{buildroot}/usr/lib/python2.7/site-packages/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/caffe
/usr/bin/classification
/usr/bin/compute_image_mean
/usr/bin/convert_cifar_data
/usr/bin/convert_imageset
/usr/bin/convert_mnist_data
/usr/bin/convert_mnist_siamese_data
/usr/bin/device_query
/usr/bin/extract_features
/usr/bin/finetune_net
/usr/bin/net_speed_benchmark
/usr/bin/test_net
/usr/bin/train_net
/usr/bin/upgrade_net_proto_binary
/usr/bin/upgrade_net_proto_text
/usr/bin/upgrade_solver_proto_text

%files data
%defattr(-,root,root,-)
/usr/share/Caffe/CaffeConfig.cmake
/usr/share/Caffe/CaffeTargets-relwithdebinfo.cmake
/usr/share/Caffe/CaffeTargets.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/caffe/blob.hpp
/usr/include/caffe/caffe.hpp
/usr/include/caffe/common.hpp
/usr/include/caffe/data_reader.hpp
/usr/include/caffe/data_transformer.hpp
/usr/include/caffe/filler.hpp
/usr/include/caffe/internal_thread.hpp
/usr/include/caffe/layer.hpp
/usr/include/caffe/layer_factory.hpp
/usr/include/caffe/layers/absval_layer.hpp
/usr/include/caffe/layers/accuracy_layer.hpp
/usr/include/caffe/layers/argmax_layer.hpp
/usr/include/caffe/layers/base_conv_layer.hpp
/usr/include/caffe/layers/base_data_layer.hpp
/usr/include/caffe/layers/batch_norm_layer.hpp
/usr/include/caffe/layers/batch_reindex_layer.hpp
/usr/include/caffe/layers/bias_layer.hpp
/usr/include/caffe/layers/bnll_layer.hpp
/usr/include/caffe/layers/concat_layer.hpp
/usr/include/caffe/layers/contrastive_loss_layer.hpp
/usr/include/caffe/layers/conv_layer.hpp
/usr/include/caffe/layers/crop_layer.hpp
/usr/include/caffe/layers/cudnn_conv_layer.hpp
/usr/include/caffe/layers/cudnn_lcn_layer.hpp
/usr/include/caffe/layers/cudnn_lrn_layer.hpp
/usr/include/caffe/layers/cudnn_pooling_layer.hpp
/usr/include/caffe/layers/cudnn_relu_layer.hpp
/usr/include/caffe/layers/cudnn_sigmoid_layer.hpp
/usr/include/caffe/layers/cudnn_softmax_layer.hpp
/usr/include/caffe/layers/cudnn_tanh_layer.hpp
/usr/include/caffe/layers/data_layer.hpp
/usr/include/caffe/layers/deconv_layer.hpp
/usr/include/caffe/layers/dropout_layer.hpp
/usr/include/caffe/layers/dummy_data_layer.hpp
/usr/include/caffe/layers/eltwise_layer.hpp
/usr/include/caffe/layers/elu_layer.hpp
/usr/include/caffe/layers/embed_layer.hpp
/usr/include/caffe/layers/euclidean_loss_layer.hpp
/usr/include/caffe/layers/exp_layer.hpp
/usr/include/caffe/layers/filter_layer.hpp
/usr/include/caffe/layers/flatten_layer.hpp
/usr/include/caffe/layers/hdf5_data_layer.hpp
/usr/include/caffe/layers/hdf5_output_layer.hpp
/usr/include/caffe/layers/hinge_loss_layer.hpp
/usr/include/caffe/layers/im2col_layer.hpp
/usr/include/caffe/layers/image_data_layer.hpp
/usr/include/caffe/layers/infogain_loss_layer.hpp
/usr/include/caffe/layers/inner_product_layer.hpp
/usr/include/caffe/layers/input_layer.hpp
/usr/include/caffe/layers/log_layer.hpp
/usr/include/caffe/layers/loss_layer.hpp
/usr/include/caffe/layers/lrn_layer.hpp
/usr/include/caffe/layers/lstm_layer.hpp
/usr/include/caffe/layers/memory_data_layer.hpp
/usr/include/caffe/layers/multinomial_logistic_loss_layer.hpp
/usr/include/caffe/layers/mvn_layer.hpp
/usr/include/caffe/layers/neuron_layer.hpp
/usr/include/caffe/layers/parameter_layer.hpp
/usr/include/caffe/layers/pooling_layer.hpp
/usr/include/caffe/layers/power_layer.hpp
/usr/include/caffe/layers/prelu_layer.hpp
/usr/include/caffe/layers/python_layer.hpp
/usr/include/caffe/layers/recurrent_layer.hpp
/usr/include/caffe/layers/reduction_layer.hpp
/usr/include/caffe/layers/relu_layer.hpp
/usr/include/caffe/layers/reshape_layer.hpp
/usr/include/caffe/layers/rnn_layer.hpp
/usr/include/caffe/layers/scale_layer.hpp
/usr/include/caffe/layers/sigmoid_cross_entropy_loss_layer.hpp
/usr/include/caffe/layers/sigmoid_layer.hpp
/usr/include/caffe/layers/silence_layer.hpp
/usr/include/caffe/layers/slice_layer.hpp
/usr/include/caffe/layers/softmax_layer.hpp
/usr/include/caffe/layers/softmax_loss_layer.hpp
/usr/include/caffe/layers/split_layer.hpp
/usr/include/caffe/layers/spp_layer.hpp
/usr/include/caffe/layers/tanh_layer.hpp
/usr/include/caffe/layers/threshold_layer.hpp
/usr/include/caffe/layers/tile_layer.hpp
/usr/include/caffe/layers/window_data_layer.hpp
/usr/include/caffe/net.hpp
/usr/include/caffe/parallel.hpp
/usr/include/caffe/proto/caffe.pb.h
/usr/include/caffe/sgd_solvers.hpp
/usr/include/caffe/solver.hpp
/usr/include/caffe/solver_factory.hpp
/usr/include/caffe/syncedmem.hpp
/usr/include/caffe/test/test_caffe_main.hpp
/usr/include/caffe/test/test_gradient_check_util.hpp
/usr/include/caffe/util/benchmark.hpp
/usr/include/caffe/util/blocking_queue.hpp
/usr/include/caffe/util/cudnn.hpp
/usr/include/caffe/util/db.hpp
/usr/include/caffe/util/db_leveldb.hpp
/usr/include/caffe/util/db_lmdb.hpp
/usr/include/caffe/util/device_alternate.hpp
/usr/include/caffe/util/format.hpp
/usr/include/caffe/util/gpu_util.cuh
/usr/include/caffe/util/hdf5.hpp
/usr/include/caffe/util/im2col.hpp
/usr/include/caffe/util/insert_splits.hpp
/usr/include/caffe/util/io.hpp
/usr/include/caffe/util/math_functions.hpp
/usr/include/caffe/util/mkl_alternate.hpp
/usr/include/caffe/util/rng.hpp
/usr/include/caffe/util/signal_handler.h
/usr/include/caffe/util/threading.hpp
/usr/include/caffe/util/upgrade_proto.hpp
/usr/lib64/libcaffe.so

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcaffe.so.1.0.0-rc3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/caffe/LICENSE

%files python
%defattr(-,root,root,-)
