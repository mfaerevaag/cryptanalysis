//
//  AppDelegate.m
//  FreqAnalysis
//
//  Created by Markus Færevaag on 12.06.13.
//  Copyright (c) 2013 Markus Færevaag. All rights reserved.
//

#import "AppDelegate.h"
#import "MainViewController.h"

@interface AppDelegate ()
@property (nonatomic, strong) IBOutlet MainViewController *mainViewController;

@end

@implementation AppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    // Init
    self.mainViewController = [[MainViewController alloc] initWithNibName:@"MainViewController" bundle:nil];
    
    // Add to windows content
    [self.window.contentView addSubview:self.mainViewController.view];
    self.mainViewController.view.frame = ((NSView *)self.window.contentView).bounds;
}

@end
