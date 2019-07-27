/*
 * IRandom.h
 *
 * This source file is part of the FoundationDB open source project
 *
 * Copyright 2013-2018 Apple Inc. and the FoundationDB project authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "fdbrpc/fdbrpc.h"
#include "fdbrpc/PerfMetric.h"
#include "flow/SerializeImpl.h"

MAKE_SERIALIZABLE(ReplyPromise<Void>);
MAKE_SERIALIZABLE(ReplyPromise<double>);
MAKE_SERIALIZABLE(ReplyPromise<bool>);
MAKE_SERIALIZABLE(ReplyPromise<int8_t>);
MAKE_SERIALIZABLE(ReplyPromise<uint8_t>);
MAKE_SERIALIZABLE(ReplyPromise<int16_t>);
MAKE_SERIALIZABLE(ReplyPromise<uint16_t>);
MAKE_SERIALIZABLE(ReplyPromise<int32_t>);
MAKE_SERIALIZABLE(ReplyPromise<uint32_t>);
MAKE_SERIALIZABLE(ReplyPromise<int64_t>);
MAKE_SERIALIZABLE(ReplyPromise<uint64_t>);

MAKE_SERIALIZABLE(Endpoint);

template struct SerializedMsg<ArenaReader, ReplyPromise<std::vector<PerfMetric>>>;
template struct ObjectSerializedMsg<ErrorOr<EnsureTable<std::pair<long, long>>>>;
