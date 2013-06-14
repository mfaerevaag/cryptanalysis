//
//  Analyzer.h
//  FreqAnalysis
//
//  Created by Markus Færevaag on 12.06.13.
//  Copyright (c) 2013 Markus Færevaag. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface Analyzer : NSObject

@property (readonly, nonatomic) NSMutableDictionary *entries;

- (void) analyzeContent: (NSString *)content;

@end
