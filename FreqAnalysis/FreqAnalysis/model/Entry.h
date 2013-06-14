//
//  FrequencyEntry.h
//  FreqAnalysis
//
//  Created by Markus Færevaag on 12.06.13.
//  Copyright (c) 2013 Markus Færevaag. All rights reserved.
//

#import <Foundation/Foundation.h>

typedef enum {
    Monogram = 1,
    Bigram = 2,
    Trigram = 3
} EntryType;

@interface Entry : NSObject

@property (copy) NSString *value;
@property EntryType type;
@property NSUInteger occurences;
@property NSNumber *frequency;

- (id) initWithValue: (NSString *)value
       andOccurences: (NSUInteger)occurences
        andFrequency: (NSNumber *)frequency;

+ (NSString *) typeToString: (EntryType)type;

@end
